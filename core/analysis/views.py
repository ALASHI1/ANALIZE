# stocks/views.py

from django.http import JsonResponse
import boto3
import requests
from decouple import config


def analyze_sentiments(text):
    comprehend = boto3.client(service_name='comprehend', region_name=config('REGION_NAME'), aws_access_key_id=config('AWS_ACCESS_KEY_ID'), aws_secret_access_key=config('AWS_SECRET_ACCESS_KEY'))
    sentiment = comprehend.detect_sentiment(Text=text, LanguageCode='en')
    return sentiment['SentimentScore']

def get_news(query):
    url = f'https://newsapi.org/v2/everything?q={query}&apiKey=932b46e97ebd4fe6a628ff37a5f14b1a'
    response = requests.get(url)
    articles = response.json().get('articles', [])
    return articles

def analyze_articles(articles):
    valid_articles = [article for article in articles if isinstance(article['description'], str) and len(article['description']) > 0][:10]
    sentiments = [analyze_sentiments(article['description']) for article in valid_articles]
    average_sentiment = calculate_average_sentiments(sentiments)
    return average_sentiment

def calculate_average_sentiments(sentiments):
    total_positive = 0
    total_negative = 0
    total_neutral = 0
    total_mixed = 0
    count = len(sentiments)
    for sentiment in sentiments:
        total_positive += sentiment.get('Positive', 0)
        total_negative += sentiment.get('Negative', 0)
        total_neutral += sentiment.get('Neutral', 0)
        total_mixed += sentiment.get('Mixed', 0)
    average_sentiments = {
        'Positive': round((total_positive / count) * 100, 2),
        'Negative': round((total_negative / count) * 100, 2),
        'Neutral': round((total_neutral / count) * 100, 2),
        'Mixed': round((total_mixed / count) * 100, 2)
    }
    return average_sentiments


def get_stock_sentiment(request, symbol):
    articles = get_news(symbol)
    text = [str(article['description']) for article in articles]
    sentiment = analyze_articles(articles)
    return JsonResponse({'symbol': symbol, 'sentiment': sentiment})

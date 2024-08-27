from django.shortcuts import render
from datetime import datetime, timedelta
import yfinance as yf
from django.http import JsonResponse
from requests_html import HTMLSession
from yahoo_fin import stock_info as s
import requests
import json

def get_jsonparsed_data(url):
    """
    Receive the content of ``url``, parse it as JSON, and return the object.

    Parameters
    ----------
    url : str

    Returns
    -------
    dict
    """
    response = requests.get(url)
    response.raise_for_status()  # Raises an HTTPError if the HTTP request returned an unsuccessful status code
    return response.json()




def get_popular_stocks(request):
    url = "https://financialmodelingprep.com/api/v3/stock_market/gainers?apikey=4VuOIgUpZwTIKepS5Ac6JcrZB3mlLVuA"
    data = get_jsonparsed_data(url)
    print(json.dumps(data, indent=4))

    

    return render(request, 'accounts/test.html', {'data': "data"})
# Create your views here.


def home(request):
    gainers = get_gainers()
    losers = get_losers()
    get_market_trend = market_trend()
    return render(request, 'accounts/home.html',{
        'gainers': gainers,
        'losers': losers,
        'dates': get_market_trend['dates'],
        'average_changes': get_market_trend['average_changes'],
    })

def about(request):
    return render(request, 'accounts/about.html')



API_KEY = "YOUR_API_KEY"
SYMBOLS = ["SPY", "DIA", "QQQ"]  # Example symbols: S&P 500, Dow Jones, NASDAQ ETFs

def get_historical_data(symbol):
    end_date = datetime.now().strftime('%Y-%m-%d')
    start_date = (datetime.now() - timedelta(days=7)).strftime('%Y-%m-%d')
    url = f"https://financialmodelingprep.com/api/v3/historical-price-full/{symbol}?from={start_date}&to={end_date}&apikey=4VuOIgUpZwTIKepS5Ac6JcrZB3mlLVuA"
    response = requests.get(url)
    return response.json()

def test(request):
    return render(request, 'accounts/test.html')


def market_trend():
    aggregate_changes = []
    dates = []

    for symbol in SYMBOLS:
        data = get_historical_data(symbol)
        if 'historical' in data:
            percentage_changes = []
            for day in data['historical']:
                percentage_change = ((day['close'] - day['open']) / day['open']) * 100
                percentage_changes.append(percentage_change)
            aggregate_changes.append(percentage_changes)
            if not dates:
                dates = [day['date'] for day in data['historical']]
        else:
            print(f"Missing data for {symbol}")

    if aggregate_changes:
        average_changes = [sum(x) / len(x) for x in zip(*aggregate_changes)]
    else:
        average_changes = []

    context = {
        'dates': dates[::-1],
        'average_changes': average_changes[::-1],
    }
    return context


def get_popular_stocks(request):
    gainers = get_gainers(request)
    losers = get_losers(request)
    return render(request, 'accounts/test.html', {'gainers': gainers, 'losers': losers})

def get_losers():
    url = "https://financialmodelingprep.com/api/v3/stock_market/losers?apikey=4VuOIgUpZwTIKepS5Ac6JcrZB3mlLVuA"
    data = get_jsonparsed_data(url)
    return data

def get_gainers():
    url = "https://financialmodelingprep.com/api/v3/stock_market/gainers?apikey=4VuOIgUpZwTIKepS5Ac6JcrZB3mlLVuA"
    data = get_jsonparsed_data(url)
    return data
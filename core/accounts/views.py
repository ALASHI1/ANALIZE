from django.shortcuts import render
import yfinance as yf
from django.http import JsonResponse
from requests_html import HTMLSession
from yahoo_fin import stock_info as si

def get_popular_stocks(request):
    session = HTMLSession()
    most_active = si.get_day_most_active()
    gainers = si.get_day_gainers()
    losers = si.get_day_losers()
    
    data = {
    "most_active": most_active[['Symbol', 'Name', 'Price (Intraday)', '% Change']].rename(columns={'Price': 'Price', '% Change': 'Change'}).to_dict('records')[:5],
    "gainers": gainers[['Symbol', 'Name', 'Price (Intraday)', '% Change']].rename(columns={'Price': 'Price', '% Change': 'Change'}).to_dict('records')[:5],
    "losers": losers[['Symbol', 'Name', 'Price (Intraday)', '% Change']].rename(columns={'Price': 'Price', '% Change': 'Change'}).to_dict('records')[:5],
}
    return render(request, 'accounts/test.html', {'data': data})
# Create your views here.


def home(request):
    return render(request, 'accounts/home.html')

def about(request):
    return render(request, 'accounts/about.html')

def test(request):
    session = HTMLSession()
    most_active = si.get_day_most_active()
    gainers = si.get_day_gainers()
    losers = si.get_day_losers()
    
    data = {
    "most_active": most_active[['Symbol', 'Name', 'Price (Intraday)', '% Change']].rename(columns={'Price (Intraday)': 'Price', '% Change': 'Change'}).to_dict('records')[:5],
    "gainers": gainers[['Symbol', 'Name', 'Price (Intraday)', '% Change']].rename(columns={'Price (Intraday)': 'Price', '% Change': 'Change'}).to_dict('records')[:5],
    "losers": losers[['Symbol', 'Name', 'Price (Intraday)', '% Change']].rename(columns={'Price (Intraday)': 'Price', '% Change': 'Change'}).to_dict('records')[:5],
}
    return render(request, 'accounts/test.html', {'data': data})
from django.shortcuts import render
import yfinance as yf
from django.http import JsonResponse
from requests_html import HTMLSession
from yahoo_fin import stock_info as si
from .models import Tickers
from .forms import TickerListForm

def get_popular_stocks(request):
    session = HTMLSession()
    most_active = si.get_day_most_active()
    gainers = si.get_day_gainers()
    losers = si.get_day_losers()
    
    data = {
    "most_active": most_active.to_dict('records')[:5],
    "gainers": gainers.to_dict('records')[:5],
    "losers": losers.to_dict('records')[:5],
}


    return JsonResponse(data)

def get_stock_data(request, symbol):
    data = get_realtime_data(symbol)
    print(data)
    return JsonResponse(data)

# def get_realtime_data(ticker):
#     stock = yf.Ticker(ticker)
#     hist = stock.history(period="1d")
#     current_price = hist['Close'].iloc[-1]
#     price_change = hist['Close'].pct_change().iloc[-1] * 100 

#     return {
#         "price": current_price,
#         "change": price_change
#     }

def get_realtime_data(symbol):
    stock = yf.Ticker(symbol)
    data = stock.history(period='1d', interval='1m')
    latest_data = data.iloc[-1].to_dict()
    return latest_data

def get_stock_info_view(request, symbol):
    data = get_stock_info(symbol)
    return JsonResponse(data)

def get_stock_info(symbol):
    stock = yf.Ticker(symbol)
    data = stock.info
    return data

def get_stock_dividends(request, symbol):
    stock = yf.Ticker(symbol)
    data = stock.dividends
    return JsonResponse(data.to_json())

def get_stock_splits(request, symbol):
    stock = yf.Ticker(symbol)
    data = stock.splits
    return JsonResponse(data.to_json())

def get_stock_actions(request, symbol):
    stock = yf.Ticker(symbol)
    data = stock.actions
    return JsonResponse(data.to_json())

def get_stock_recommendations(request, symbol):
    stock = yf.Ticker(symbol)
    data = stock.recommendations
    return JsonResponse(data.to_json())

def get_stock_calendar(request, symbol):
    stock = yf.Ticker(symbol)
    data = stock.calendar
    print(data)
    return JsonResponse(data)

def get_stock_history(request, symbol, period):
    stock = yf.Ticker(symbol)
    data = stock.history(period=period) # period = 1d, 5d, 1mo, 3mo, 6mo, 1y, 2y, 5y, 10y, ytd, max
    return JsonResponse(data.to_json())
   
def get_comparison_data_view(request):
    form = TickerListForm()
    if request.method == 'POST':
        form = TickerListForm(request.POST)
        if form.is_valid():
            tickers = form.cleaned_data['tickers']
            period = form.cleaned_data['period']
            data = get_comparison_data(tickers)
            return JsonResponse(data, safe=False)
    return render(request, 'stocks/comparison.html', {'form': form})


def get_comparison_data(tickers,period="5d"):    
    data = {}
    for ticker in tickers:
        stock = yf.Ticker(ticker)
        history = stock.history(period=period)
        data[ticker] = history.to_dict('records')
    return data


def view_boards(request):
    return render(request, 'stocks/board.html')
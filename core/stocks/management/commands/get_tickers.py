import pandas as pd
import requests
import csv
from django.core.management.base import BaseCommand
from stocks.models import Tickers
from stocks import views


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        symbols = get_sp500_symbols()
        df_symbols = pd.DataFrame(symbols, columns=['Symbol'])
        csv_file_path = 'sp500_symbols.csv'
        df_symbols.to_csv(csv_file_path, index=False)

        with open(csv_file_path, 'r') as file:
            reader = csv.reader(file)
            next(reader)  # Skip the header row
            for row in reader:
                symbol = row[0]
                info = views.get_stock_info(symbol)
                if info:  # Ensure info is not None
                    Tickers.objects.get_or_create(
                        symbol=symbol,
                        defaults={
                            'name': info.get('longName', ''),
                            'sector': info.get('sector', ''),
                            'industry': info.get('industry', ''),
                            'market_cap': info.get('marketCap', 0),
                            'website': info.get('website', ''),
                            'summary_quote': info.get('longBusinessSummary', '')
                        }
                    )

        print({'message': 'Data saved successfully!'})

# Function to get stock symbols for S&P 500 companies
def get_sp500_symbols():
    url = 'https://en.wikipedia.org/wiki/List_of_S%26P_500_companies'
    response = requests.get(url)
    response.raise_for_status()  # Raise an exception for HTTP errors
    tables = pd.read_html(response.text)
    df = tables[0]
    symbols = df['Symbol'].tolist()
    return symbols

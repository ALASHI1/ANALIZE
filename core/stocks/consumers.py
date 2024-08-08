import json
from channels.generic.websocket import AsyncWebsocketConsumer
import yfinance as yf
import asyncio

class StockConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()
        # Start a background task to push data every minute
        self.channel_layer = self.channel_layer
        await self.send_stock_data()
        
    async def disconnect(self, close_code):
        # Clean up any background tasks if needed
        pass

    async def send_stock_data(self):
        while True:
            data = await self.get_stock_data()
            await self.send(text_data=json.dumps(data))
            await asyncio.sleep(60)  # Sleep for 1 minute

    async def get_stock_data(self):
        # Fetch stock data from yfinance
        stocks = ["NVDA", "AAPL", "GOOGL"]  # Example stock symbols
        stock_data = {}
        for stock in stocks:
            ticker = yf.Ticker(stock)
            info = ticker.info
            stock_data[stock] = {
                "Symbol": stock,
                "Price": info.get('currentPrice', 'N/A'),
                "Change": info.get('regularMarketChange', 'N/A'),
                "Percent Change": info.get('regularMarketChangePercent', 'N/A')
            }
        return stock_data

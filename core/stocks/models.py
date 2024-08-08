from django.db import models

# Create your models here.

class Tickers(models.Model):
    symbol = models.CharField(max_length=10)
    name = models.CharField(max_length=100)
    market_cap = models.CharField(max_length=100)
    website = models.CharField(max_length=100)
    sector = models.CharField(max_length=100)
    industry = models.CharField(max_length=100)
    summary_quote = models.CharField(max_length=100)
    def __str__(self):
        return self.symbol
    
    
    
class Stocks(models.Model):
    symbol = models.CharField(max_length=10)
    name = models.CharField(max_length=100)
    market_cap = models.CharField(max_length=100)
    website = models.CharField(max_length=100)
    sector = models.CharField(max_length=100)
    industry = models.CharField(max_length=100)
    summary_quote = models.CharField(max_length=100)
    def __str__(self):
        return self.symbol
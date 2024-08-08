from django.contrib import admin
from .models import Tickers
# Register your models here.


@admin.register(Tickers)
class TickersAdmin(admin.ModelAdmin):
    list_display = ('symbol', 'name', 'sector', 'industry', 'market_cap', 'website')
    search_fields = ('symbol', 'name', 'sector', 'industry')
    list_filter = ('sector', 'industry')
    list_per_page = 10
    ordering = ('symbol',)
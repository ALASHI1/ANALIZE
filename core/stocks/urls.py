from django.urls import path
from stocks import views


urlpatterns = [
    path('data/<str:symbol>/', views.get_stock_data, name='get_stock_data'),
    path('info/<str:symbol>/', views.get_stock_info_view, name='get_stock_info'),
    path('dividends/<str:symbol>/', views.get_stock_dividends, name='get_stock_dividends'),
    path('splits/<str:symbol>/', views.get_stock_splits, name='get_stock_splits'),
    path('actions/<str:symbol>/', views.get_stock_actions, name='get_stock_actions'),
    path('recommendations/<str:symbol>/', views.get_stock_recommendations, name='get_stock_recommendations'),
    path('calendar/<str:symbol>/', views.get_stock_calendar, name='get_stock_calendar'),
    path('history/<str:symbol>/<str:period>/', views.get_stock_history, name='get_stock_history'),
    path('popular/', views.get_popular_stocks, name='get_popular_stocks'),
    path('compare/', views.get_comparison_data_view, name='compare_stocks'),
    path('board/', views.view_boards, name='view_boards'),
]
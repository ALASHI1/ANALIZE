from django.urls import path
from . import views

urlpatterns = [
    path('sentiment/<str:symbol>/', views.get_stock_sentiment, name='get_stock_sentiment'),
]
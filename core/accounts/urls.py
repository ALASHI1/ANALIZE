from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('test/', views.test, name='test'),
    path('about/', views.about, name='about'),
]
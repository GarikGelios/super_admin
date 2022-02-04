from django.urls import path
from core import views, models, forms
from django.views.generic import ListView, CreateView, UpdateView


app_name = 'main'

urlpatterns = [
    path('', views.index, name='main'),
]
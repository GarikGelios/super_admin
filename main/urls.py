from django.urls import path
from main import views, models
from django.views.generic import ListView, CreateView, UpdateView


app_name = 'main'

urlpatterns = [
    path('', views.index, name='main'),


    path('posts/', ListView.as_view(
        model=models.Post,
        template_name='main/posts/list.html'
    ), name='posts_list'),
]
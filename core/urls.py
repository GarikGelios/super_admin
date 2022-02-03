from django.urls import path
from core import views, models, forms
from django.views.generic import ListView, CreateView, UpdateView
from django.contrib.auth.decorators import login_required


app_name = 'admin'

urlpatterns = [
    path('', views.index, name='index'),

    path('users/', login_required(ListView.as_view(
        model=models.User,
        template_name='core/users/list.html'
    )), name='users_list'),

    path('users/create/', login_required(CreateView.as_view(
        model=models.User,
        form_class=forms.CreateUserForm,
        template_name='core/users/create.html',
        success_url='/admin/users/'
    )), name='users_create'),

    path('users/update/<int:pk>/', login_required(UpdateView.as_view(
        model=models.User,
        form_class=forms.UpdateUserForm,
        template_name='core/users/update.html',
        success_url='/admin/users/'
    )), name='users_update'),

    path('users/<int:pk>/change_password/', login_required(views.change_password
                                                           ), name='change_password'),

    path('users/login/', views.user_login, name='login'),

    #url(r'^login/$', views.user_login, name='login'),

    path('posts/', login_required(ListView.as_view(
        model=models.Post,
        template_name='core/posts/list.html'
    )), name='posts_list'),


    path('posts/create/', login_required(CreateView.as_view(
        model=models.Post,
        form_class=forms.CreatePostForm,
        template_name='core/posts/create.html',
        success_url='/admin/posts/'
    )), name='posts_create'),

    # Todo: add delete url
]

from django.urls import path
from core import views, models, forms
from django.views.generic import ListView, CreateView, UpdateView


app_name = 'admin'

urlpatterns = [
    path('', views.index, name='index'),

    path('users/', ListView.as_view(
        model=models.User,
        template_name='core/users/list.html'
    ), name='users_list'),

    path('users/create/', CreateView.as_view(
        model=models.User,
        form_class=forms.CreateUserForm,
        template_name='core/users/create.html',
        success_url='admin:users_list'
    ), name='users_create'),

    path('users/update/<int:pk>/', UpdateView.as_view(
        model=models.User,
        form_class=forms.UpdateUserForm,
        template_name='core/users/update.html',
        success_url='admin:users_list'
    ), name='users_update'),

    path('users/<int:pk>/change_password/', views.change_password, name='change_password'),

    path('users/login/', views.user_login, name='login'),

    #url(r'^login/$', views.user_login, name='login'),

    # Todo: add delete url
]

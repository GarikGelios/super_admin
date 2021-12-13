from django.shortcuts import render
from django.views.generic import ListView

from core import models


def index(request):
    return render(request, 'core/index.html', locals())


class UserListView(ListView):
    model = models.User

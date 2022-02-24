from django.shortcuts import render
from django.views.generic import ListView
from core.models import Post


def index(request):
    return render(request, 'main/index.html', locals())
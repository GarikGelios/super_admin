from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from core import models
from core.forms import PasswordChangeForm, LoginForm
from django.http import HttpResponse
from django.contrib.auth import authenticate, login


def index(request):
    return render(request, 'core/index.html', locals())


def change_password(request, pk):
    # Принтуй, что тебе приходит в запросе
    print(request.POST)
    # Получаем объект юзера или говорим серверу кинуть 404 HTTP ощибку, если объект не найден
    user = get_object_or_404(models.User, pk=pk)
    # Передаем юзера форме, а также направляем туда все данные HTTP метода POST, если они прилетели
    form = PasswordChangeForm(request.POST or None, user=user)
    # Т.к. в этой вьюхе обрабатывается два метода, GET и POST, их нужно отделять
    # Поэтому логику POST, при условии валидности формы, отравляем в иф
    # Смотри форму forms.PasswordChangeForm метод clean, там будут валидации, которые стартуют при вызове метода
    # form.is_valid()
    #
    # GET запрос приходит на сервер по умолчанию, а вот POST надо послать формой HTML
    # Это одна из немногих штук, как HTML влияет на радоту сервера (ито если прогрпммист это обработает)
    print(request.method == 'POST', form.is_valid())
    if request.method == 'POST' and form.is_valid():
        print('valid:', user)
        form.save()
        messages.success(request, "Password succesfully changed!")
        return redirect('admin:users_update', pk)
    return render(request, 'core/users/change_password.html', locals())


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('Authenticated successfully')
                else:
                    return HttpResponse('Invalid login')
    else:
        form = LoginForm()
    return render(request, 'core/users/login.html', {'form': form})

from django.contrib.auth.forms import PasswordChangeForm
from django.shortcuts import render, redirect


def index(request):
    return render(request, 'core/index.html', locals())


def change_password(request, pk):
    form = PasswordChangeForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('admin:users_update', pk)
    return render(request, 'core/users/change_password.html', locals())

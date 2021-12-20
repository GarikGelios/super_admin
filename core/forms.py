from django import forms

from core import models

from django.shortcuts import render, redirect


class CreateUserForm(forms.ModelForm):

    class Meta:
        model = models.User
        exclude = ['date_joined']
        widgets = {
            'password': forms.PasswordInput
        }


class UpdateUserForm(CreateUserForm):

    class Meta(CreateUserForm.Meta):
        pass

def change_pasword(request, pk):
    form = forms.ChangePassword(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('admin:users_update', pk)
    return render(request, 'core/users/change_password.html')

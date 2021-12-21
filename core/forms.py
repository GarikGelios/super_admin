from django import forms

from core import models


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


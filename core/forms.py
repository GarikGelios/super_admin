from django import forms
from django.contrib.auth import password_validation
from django.contrib.auth.forms import SetPasswordForm
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

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


class PasswordChangeForm(forms.Form):
    newpass1 = forms.CharField(
        label=_("New password"),
        widget=forms.PasswordInput(),
    )
    newpass2 = forms.CharField(
        label=_("New password confirmation"),
        widget=forms.PasswordInput(),
    )

    # Конструктор класса, мы его переписываем что-бы иметь возможность в форму передать юзера
    # Юзера надо добавить в контекст self до вызова super, потому что в родительском классе его нет и вылетит эксепшн
    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super().__init__(*args, **kwargs)

    # В этом методе мы делаем все валидации формы
    # https://docs.djangoproject.com/en/4.0/ref/forms/validation/
    # Официальная дока, ну или найди себе какой видос/мануал, про валидацию форм.
    def clean(self, *args, **kwargs):
        print(args, kwargs)
        password1 = self.cleaned_data.get('newpass1')
        password2 = self.cleaned_data.get('newpass2')
        if password1 and password2:
            if password1 != password2:
                raise ValidationError(
                    _('The two password fields didn’t match.')
                )
        return self.cleaned_data

    # Этот метод небходим для сохранения данных формы в базу
    # Его ты вызываешь во въюхе.
    def save(self, commit=True):
        password = self.cleaned_data["newpass1"]
        # set_password это стандартный метод модели юзера (где-то в родительских классах он описан).
        # Он хэширует пароль необратимым (односторонним) шифрованием, чтобы в базе лежал только его хеш.
        # Это используется для защиты пользователей, чтоюы даже адмены сайта не могли зайти в аккаунт юзера, ну точнее
        # не знали пароль, зайти то они скорей всего смогут=))
        # https://docs.djangoproject.com/en/4.0/topics/auth/customizing/#django.contrib.auth.models.AbstractBaseUser.set_password
        self.user.set_password(password)
        if commit:
            self.user.save()
        return self.user


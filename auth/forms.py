from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    username = forms.CharField(
        label="Имя пользователя",
        max_length=30,
        required=True,
        help_text=False)
    password1 = forms.CharField(
        label="Придумайте пароль",
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
        help_text=False,
    )
    password2 = forms.CharField(
        label="Подтвердите пароль",
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
        strip=False,
        help_text=False,
    )

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', )
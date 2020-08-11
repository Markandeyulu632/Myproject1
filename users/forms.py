from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UserRegisterForm(UserCreationForm):
    first_name = forms.CharField()
    last_name = forms.CharField()
    pnumber = forms.IntegerField(max_value=9999999999)
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'password1', 'password2', 'email', 'pnumber']
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db import models


class RegistrationForm(UserCreationForm):
    username = models.CharField(max_length=150,)
    email = models.EmailField(max_length=50,)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegistrationForm(UserCreationForm):
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username',]

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

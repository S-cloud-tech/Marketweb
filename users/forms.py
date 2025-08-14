from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import User

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('email', 'password1', 'password2')

class CustomLoginForm(AuthenticationForm):
    username = forms.CharField(label='Enter your Email...')


from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm 
# from .models import User

# class CustomUserCreationForm(UserCreationForm):
#     class Meta:
#         model = User
#         fields = ('username', 'email')

class CustomLoginForm(AuthenticationForm):
    username = forms.CharField(label='Enter your Email...')


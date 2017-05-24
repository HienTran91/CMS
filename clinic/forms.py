from django.contrib.auth.forms import AuthenticationForm 
from django import forms

# If you don't do this you cannot use Bootstrap CSS
class LoginForm(AuthenticationForm):
    username = forms.CharField(label="Username", widget=forms.TextInput(attrs={'class': 'form-control','placeholder': 'User name or email address', 'name': 'username'}))
    password = forms.CharField(label="Password", widget=forms.PasswordInput(attrs={'class': 'form-control','placeholder': 'Password', 'name': 'password'}))
from socket import fromshare
from django import forms
from .models import Users
from django.contrib.auth.password_validation import validate_password

class RegistForm(forms.ModelForm):
    username = forms.CharField(label="Name")
    age = forms.IntegerField(label="Age", min_value=0)
    email = forms.EmailField(label="E-mail")
    pasword = forms.CharField(label="Password", widget=forms.PasswordInput)
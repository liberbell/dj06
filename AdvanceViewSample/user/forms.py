from dataclasses import fields
from django import forms
from django.contrib.auth.models import User
from user.models import Profile

class UserForm(forms.ModelForm):
    username = forms.CharField(label="Name")
    email = forms.EmailField(label="E-Mail")
    password = forms.CharField(label="Password", widget=forms.PasswordInput())
    
    class Meta():
        model = User
        fields = ("username", "email", "password")

class ProfileForm(forms.ModelForm):
    website = forms.URLField(label="HomePage")
    picture = forms.FileField(label="Picture")

    class Meta():
        model = Profile
        fields = ("website", "picture")

class LoginForm(forms.Form):
    username = forms.CharField(max_length=50, label="Name")
    password = forms.CharField(label="Password", widget=forms.PasswordInput())
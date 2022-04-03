from django import forms
from .models import Users

class RegistForm(forms.ModelForm):
    username = forms.CharField(label="name")
    age = forms.IntegerField(label="Age", min_value=0)
    email = forms.EmailField(label="E-Mail")
    password = forms.CharField(label="Password", widget=forms.PasswordInput)
    confirm_password = forms.CharField(label="Re-enter Password", widget=forms.PasswordInput)

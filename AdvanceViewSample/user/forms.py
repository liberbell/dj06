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
    confirm_password = forms.CharField(label="Confirm Password", widget=forms.PasswordInput())

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data["password"]
        confirm_password = cleaned_data["confirm_password"]
        if password != confirm_password:
            raise forms.ValidationError("Don`t mutch password.")
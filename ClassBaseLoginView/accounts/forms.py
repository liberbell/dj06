from socket import fromshare
from django import forms
from .models import Users
from django.contrib.auth.password_validation import validate_password

class RegistForm(forms.ModelForm):
    username = forms.CharField(label="Name")
    age = forms.IntegerField(label="Age", min_value=0)
    email = forms.EmailField(label="E-mail")
    password = forms.CharField(label="Password", widget=forms.PasswordInput)

    class Meta:
        model = Users
        fields = ["username", "age", "email", "password"]

    def save(self, commit=False):
        user = super().save(commit=False)
        validate_password(self.cleaned_data["password"], user)
        user.set_password(self.cleaned_data["password"])
        user.save()
        return user
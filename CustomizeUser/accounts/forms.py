from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError

User = get_user_model()

class UserCreationForm(forms.ModelForm):
    Password = forms.CharField(label="password", widget=forms.PasswordInput)
    Confirm_password = forms.CharField(label="confirm password", widget=forms.PasswordInput)
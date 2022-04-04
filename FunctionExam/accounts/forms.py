from django import forms
from .models import Users

class RegistForm(forms.ModelForm):
    username = forms.CharField(label="name")
    age = forms.IntegerField(label="Age", min_value=0)
    email = forms.EmailField(label="E-Mail")
    password = forms.CharField(label="Password", widget=forms.PasswordInput)
    confirm_password = forms.CharField(label="Re-enter Password", widget=forms.PasswordInput)

    class Meta():
        model = Users
        fields = {"username", "age", "email", "password"}

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data["password"]
        confirm_password = cleaned_data["confirm_password"]

        if password != confirm_password:
            raise forms.ValidationError("Password not match.")

from django.shortcuts import render, redirect
from . import forms
from django.core.exceptions import ValidationError

# Create your views here.
def home(request):
    return render(
        request, "accounts/home.html"
    )

def regist(request):
    regist_form = forms.RegistForm(request.POST or None)
    if regist_form.is_valid():
        try:
            regist_form.save()
            return redirect("accounts:home")
        except ValidationError as err:
            regist_form.add_error("password", err)

    return render(
        request, 'accouonts/register.html', context={
            'regist_form': regist_form
        }
    )


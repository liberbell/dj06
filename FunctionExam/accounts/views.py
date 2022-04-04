from django.shortcuts import render
from . import forms

# Create your views here.
def home(request):
    return render(
        request, "accounts/home.html"
    )

def regist(request):
    regist_form = forms.RegistForm(request.POST or None)
    if regist_form.is_valid():
        regist_form.save()


    return render(
        request, 'accouonts/register.html', context={
            'regist_form': regist_form
        }
    )


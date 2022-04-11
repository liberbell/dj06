from django.shortcuts import render
from . import forms

# Create your views here.
def create_theme(request):
    create_theme_form = forms.CreateThemeForm(request.POST or None)
    if create_theme_form.is_valid():
        pass
    return render(request, "boards/create_theme.html", context={
        "create_theme_form": create_theme_form
    })
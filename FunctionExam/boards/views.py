from django.shortcuts import render
from . import forms

# Create your views here.
def create_theme(request):
    create_theme_form = forms.CreateThemeForm(request.POST or None)
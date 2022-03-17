from django.shortcuts import render
from . import forms

# Create your views here.

def insert_student(request):
    insert_form = forms.StudentsInsertForm(request.POST or None, request.FILES or None)
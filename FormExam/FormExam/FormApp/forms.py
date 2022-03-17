from .models import Students
from django import forms

class StudentsInsert(forms.ModelForm):
    name = forms.CharField(label="name")
    age = forms.IntegerField(label="age")
    grade = forms.IntegerField(label="grade")
    picture = forms.FileField(label="file_upload")
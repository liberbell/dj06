from dataclasses import fields
from .models import Students
from django import forms

class StudentInsertForm(forms.ModelForm):
    name = forms.CharField(label="name")
    age = forms.IntegerField(label="age")
    grade = forms.IntegerField(label="grade")
    picture = forms.FileField(label="file_upload")

    class Meta:
        model = Students
        fields = "__all__"
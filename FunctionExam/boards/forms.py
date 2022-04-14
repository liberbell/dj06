from .models import Themes, Comments
from django import forms

class CreateThemeForm(forms.ModelForm):
    title = forms.CharField(label="Title")

    class Meta:
        model = Themes
        fields = ('title',)

class DeleteThemeForm(forms.ModelForm):
    pass
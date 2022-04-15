from .models import Themes, Comments
from django import forms

class CreateThemeForm(forms.ModelForm):
    title = forms.CharField(label="Title")

    class Meta:
        model = Themes
        fields = ('title',)

class DeleteThemeForm(forms.ModelForm):
    
    class Meta:
        model = Themes
        fields = []

class PostCommentForm(forms.ModelForm):
    comment = forms.CharField(label="", widget=forms.Textarea(attrs={'rows':5, 'cols': 60}))

    class Meta:
        model = Comments
        fields = ('comment',)
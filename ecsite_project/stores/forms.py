from django import forms
from .models import CartsItem

class CartUpdateForm(forms.ModelForm):
    quantity = forms.IntegerField()
    id = forms.CharField(widget=forms.HiddenInput)
    
    class Meta:
        model = CartsItem
        fields = ["quantity", "id"]
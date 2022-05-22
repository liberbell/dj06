from django import forms
from .models import CartsItem

class CartUpdateForm(forms.ModelForm):
    quantity = forms.IntegerField(label="stocks", min_value=1)
    id = forms.CharField(widget=forms.HiddenInput)
    
    class Meta:
        model = CartsItem
        fields = ["quantity", "id"]
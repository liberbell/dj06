from xml.dom import ValidationErr
from django import forms
from .models import CartsItem
from django.shortcuts import get_object_or_404

class CartUpdateForm(forms.ModelForm):
    quantity = forms.IntegerField(label="stocks", min_value=1)
    id = forms.CharField(widget=forms.HiddenInput)
    
    class Meta:
        model = CartsItem
        fields = ["quantity", "id"]

    def clean(self):
        clean_field(self):
            cleand_data = super().clean()
            quantity = cleand_data.get("quantity")
            id = cleand_data.get("id")
            cart_item = get_object_or_404(CartsItem, pk=id)
            if quantity > cart_item.product.stock:
                raise ValidationErr(f"Over stocks. Input under {cart_item.product.stock}.")
            return data
        
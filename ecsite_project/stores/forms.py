from email.headerregistry import Address
from xml.dom import ValidationErr
from django import forms
from .models import CartsItem, Adresses
from django.shortcuts import get_object_or_404
from django.core.exceptions import ValidationError

class CartUpdateForm(forms.ModelForm):
    quantity = forms.IntegerField(label="stocks", min_value=1)
    id = forms.CharField(widget=forms.HiddenInput)
    
    class Meta:
        model = CartsItem
        fields = ["quantity", "id"]

    def clean(self):
        cleand_data = super().clean()
        quantity = cleand_data.get("quantity")
        id = cleand_data.get("id")
        cart_item = get_object_or_404(CartsItem, pk=id)
        if quantity > cart_item.product.stock:
            raise ValidationError(f"Over stocks. Input under {cart_item.product.stock}.")

class AddressInputForm(forms.ModelForm):
    address = forms.CharField(label="Address", widget=forms.TextInput(attrs={"size": "80"}))

    class Meta:
        model = Adresses
        fields = ["zip_code", "prefecture", "address"]
        
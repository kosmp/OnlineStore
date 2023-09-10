from django import forms
from .models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'model', 'cost', 'type', 'model', 'description', 'produced', 'image']
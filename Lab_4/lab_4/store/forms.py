from django import forms
from .models import Product, Promocode


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'model', 'cost', 'type', 'model', 'description', 'produced', 'image']


class PromocodeForm(forms.ModelForm):
    def clean(self):
        start_date = self.cleaned_data.get('start_date')

        expiration_date = self.cleaned_data.get('expiration_date')

        if (start_date > expiration_date):
            raise forms.ValidationError("Invalid promocode start and expiration dates")

        return self.cleaned_data

    class Meta:
        model = Promocode
        fields = '__all__'
from django import forms
from .models import Product, Promocode, Review
from django.core import validators


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


class ReviewForm(forms.ModelForm):
    reviewer = forms.CharField(max_length=50)

    rate = forms.IntegerField(validators=[validators.MinValueValidator(1), validators.MaxValueValidator(10)])

    text = forms.Textarea()

    class Meta:
        model = Review
        fields = ['reviewer', 'rate', 'text']
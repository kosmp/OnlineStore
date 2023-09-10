from typing import Any
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
from datetime import date, datetime

class UserCreateForm(UserCreationForm):
    first_name = forms.CharField(max_length=200,
                                help_text='Enter first name',
                                validators=[RegexValidator(
            regex=r'^[A-Za-z]+$',
            message='Name must consist of letters',
        )])
    last_name = forms.CharField(max_length=200,
                                help_text='Enter last name',
                                validators=[RegexValidator(
            regex=r'^[A-Za-z]+$',
            message='Name must consist of letters',
        )])
    address = forms.CharField(max_length=100,
                              help_text="Enter address")
    city = forms.CharField(max_length=100,
                           help_text='Enter city')

    phone_number = forms.CharField(max_length=50,
                                    help_text='Enter phone number',
                                    validators=[RegexValidator(
            regex=r'^(\+375 \([0-9]{2}\) [0-9]{3}-[0-9]{2}-[0-9]{2})$',
            message='Format +375 (XX) XXX-XX-XX',
        )])
    
    class Meta:
        model = CustomUser
        fields = {'username', 'first_name', 
                  'last_name', 'address', 'city',
                  'phone_number', 'password1', 
                  'password2'
        }

    def save(self, commit: bool = ...) -> Any:
        user = super(UserCreateForm, self).save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.city = self.cleaned_data['city']
        user.address = self.cleaned_data['address']
        user.phone_number = self.cleaned_data['phone_number']

        if commit:
            user.save()
        
        return user
    
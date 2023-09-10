from django.db import models
from .managers import CustomUserManager
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    first_name = models.CharField(max_length=200,
                                help_text='Enter first name')
    last_name = models.CharField(max_length=200,
                                help_text='Enter last name')
    address = models.CharField(max_length=100,
                               help_text='Enter address')
    city = models.CharField(max_length=100,
                            help_text='Enter city')
    phone_number = models.CharField(max_length=50,
                                    help_text='Enter phone number')
    
    objects = CustomUserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'address', 'city', 'phone_number']
    
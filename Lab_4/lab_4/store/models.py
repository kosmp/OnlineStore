from django.db import models
from django.urls import reverse

# Create your models here.

class ProductType(models.Model) :
    
    name = models.CharField(max_length=200,
                             help_text='Enter product type')
    
    def get_absolute_url(self):
        return reverse('store:product_list_by_category', args=[str(self.name)])
    
    def __str__(self) :
        return self.name
    
class Product(models.Model) :

    name = models.CharField(max_length=200)
    model = models.ForeignKey('ModelType',
                                    on_delete = models.SET_NULL,
                                    null = True)
    cost = models.IntegerField()
    type = models.ForeignKey('ProductType', 
                                on_delete = models.SET_NULL,
                                null = True)
    quantity = models.IntegerField()
    description = models.TextField()
    image = models.ImageField(upload_to='product/%Y/%m/%d', blank=True)
    purchase_count = models.PositiveIntegerField(default=0)
    produced = models.BooleanField(help_text=
                                   'True - produced, False - out of production')
    

    def get_absolute_url(self):
        return reverse('store:product_detail', args=[str(self.id)])

    def __str__(self) :
        return self.name   

class Client(models.Model) :

    first_name = models.CharField(max_length=200,
                                help_text='Enter first name')
    last_name = models.CharField(max_length=200,
                                help_text='Enter last name')

    city = models.CharField(max_length=100,
                            help_text='Enter client city') 
    address = models.CharField(max_length=100,
                               help_text='Enter client address')
    phone_number = models.CharField(max_length=50,
                                    help_text='Enter phone number')
    
    def get_absolute_url(self):
        return reverse('client-detail', args=[str(self.id)])

    def __str__(self) :
        return '{0}, {1}'.format(self.first_name, self.last_name) 


class ModelType(models.Model):
    name = models.CharField(max_length=200,
                            help_text='Enter model name')

    def get_absolute_url(self):
        return reverse('modelType-detail', args=[str(self.id)])

    def __str__(self) :
        return self.name 

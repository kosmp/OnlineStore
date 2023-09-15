from django.db import models
from django.urls import reverse
from django.core.validators import RegexValidator

# Create your models here.


class Article(models.Model):
    title = models.CharField(max_length=100, help_text="enter title of the article")

    summury = models.TextField(max_length=500, help_text="enter summury of the article")

    image = models.ImageField(upload_to="images/article_photos/", help_text="Enter article photo")

    content = models.TextField(help_text="enter content of the article")

    creation_date = models.DateTimeField(auto_now_add=True)


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


class Position(models.Model):
    name = models.CharField(max_length=20, help_text="Enter a position")

    def __str__(self):
        return self.name


class Employee(models.Model):
    user_name = models.CharField(max_length=20, help_text="Enter user name")

    photo = models.ImageField(upload_to="images/profile_photos/", help_text="Enter profile photo")

    first_name = models.CharField(max_length=20, help_text="Enter full name")

    last_name = models.CharField(max_length=20, help_text="Enter last name")

    num_validator = RegexValidator(regex=r"^\+375 \(29\) \d{3}-\d{2}-\d{2}$")

    phone_number = models.CharField(max_length=20, validators=[num_validator], default='+375 (29) xxx-xx-xx')

    position = models.ForeignKey('Position', on_delete=models.CASCADE, related_name="employee")

    def __str__(self):
        return f"{self.last_name} {self.position}"


class Vacancy(models.Model):
    position = models.CharField(max_length=50, help_text="enter employee position")

    company_name = models.CharField(max_length=50, help_text="enter company name")

    city = models.CharField(max_length=50, help_text="enter city")

    job_character = models.CharField(max_length=50, help_text="enter job character")

    schedule = models.CharField(max_length=50, help_text="enter schedule")

    employment = models.CharField(max_length=50, help_text="enter employement")

    experience = models.CharField(max_length=50, help_text="enter experience")

    education = models.CharField(max_length=50, help_text="enter education")

    description = models.TextField(help_text="enter vacancy description")

    salary = models.CharField(max_length=50, help_text="enter salary")

    def __str__(self):
        return f"{self.position} {self.company_name}"


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


class Promocode(models.Model):
    code = models.CharField(max_length=50, help_text="enter Promocode")

    start_date = models.DateTimeField()

    expiration_date = models.DateTimeField()

    def __str__(self):
        return self.code


class FAQ(models.Model):
    question = models.CharField(max_length=255)
    answer = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.question
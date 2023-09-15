from django.contrib import admin
from .models import Product, ModelType, ProductType, Client, Article, Employee, Position, Promocode, FAQ, Vacancy, Review
from .forms import PromocodeForm


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin) :
    list_display = ['name', 'model', 'image', 'cost', 'type', 'description']
    list_filter = ['model', 'type', 'purchase_count']


@admin.register(ModelType)
class ProducerAdmin(admin.ModelAdmin) :
    list_display = ['name']


@admin.register(ProductType)
class ProductTypeAdmin(admin.ModelAdmin) :
    list_display = ['name']


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin) :
    list_display = ['first_name', 'last_name', 'address',
                    'city', 'phone_number']
    list_filter = ['city']


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    pass


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('user_name', 'first_name', 'last_name', 'phone_number', 'position')


@admin.register(Position)
class PositionAdmin(admin.ModelAdmin):
    pass


@admin.register(Promocode)
class PromocodeAdmin(admin.ModelAdmin):
    list_display = ('code', 'start_date', 'expiration_date')

    form = PromocodeForm

@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = ('question', 'answer', 'date_added')


@admin.register(Vacancy)
class VacancyAdmin(admin.ModelAdmin):
    pass


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    pass
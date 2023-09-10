'''from django.contrib import admin
from .forms import UserCreateForm
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import CustomUser'''
from django.contrib import admin
from django.contrib.auth import get_user_model

User = get_user_model()
admin.site.register(User)
'''admin.site.register(CustomUser, UserAdmin)
class CustomUserAdmin(UserAdmin):
    add_form = UserCreateForm
    fieldsets = (
        ('Personal info', {'fields' : ('first_name', 'last_name', 'email')}),
        ('Survey data', {'fields' : ('date_of_birth', 'phone_number')}),
    )

# Зарегистрируйте вашу административную форму
admin.site.unregister(User)
admin.site.register(CustomUser, CustomUserAdmin)'''

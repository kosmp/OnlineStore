from django.contrib.auth.models import BaseUserManager

class CustomUserManager(BaseUserManager):
    def create_user(self, first_name, last_name, address, city, phone_number, password=None, **extra_fields):
        """
        Создает и сохраняет обычного пользователя с указанными данными.
        """

        user = self.model(first_name=first_name, last_name=last_name, 
                          address=address, city=city, phone_number=phone_number, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    #def create_superuser(self, email, first_name, last_name, date_of_birth, phone_number, password=None, **extra_fields):
    def create_superuser(self, first_name='', last_name='', address='', city='', phone_number='123', password=None, **extra_fields):
        """
        Создает и сохраняет суперпользователя с указанными данными.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(first_name, last_name, address, city, phone_number, password, **extra_fields)
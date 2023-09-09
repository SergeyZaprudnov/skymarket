from django.contrib.auth.models import AbstractBaseUser, AbstractUser
from django.db import models
from .managers import UserManager
from phonenumber_field.modelfields import PhoneNumberField
from django.utils.translation import gettext_lazy as _


class UserRoles(models.TextChoices):
    USER = 'user', _('user')  # Пользователь
    ADMIN = 'admin', _('admin')  # Администратор


class User(AbstractBaseUser):
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'phone', 'role']

    objects = UserManager()

    first_name = models.CharField(max_length=50, verbose_name='Имя')
    last_name = models.CharField(max_length=100, verbose_name='Фамилия')
    phone = PhoneNumberField(unique=True, verbose_name='Номер телефона')
    email = models.EmailField(unique=True, verbose_name='Электронная почта')
    role = models.CharField(max_length=15, choices=UserRoles.choices, default=UserRoles.USER,
                            verbose_name='Роль пользователя')
    image = models.ImageField(upload_to='avatars/', blank=True, null=True, verbose_name='Аватарка')
    is_active = models.BooleanField(default=True, verbose_name='Действующий')

    def __str__(self):
        return f'{self.email}'

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    @property
    def is_admin(self):
        return self.role == UserRoles.ADMIN

    @property
    def is_user(self):
        return self.role == UserRoles.USER

    @property
    def is_superuser(self):
        return self.is_admin

    @property
    def is_staff(self):
        return self.is_admin

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return self.is_admin

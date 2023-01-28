from django.db import models
from constant.models import Nationality, Education
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager


class CustomAccountManager(BaseUserManager):
    use_in_migrations = True

    def create_superuser(self, first_name, last_name, email, password, **other_fields):

        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        # other_fields.setdefault('is_active', True)

        if other_fields.get('is_staff') is not True:
            raise ValueError(
                'Superuser must be assigned to is_staff=True.')
        if other_fields.get('is_superuser') is not True:
            raise ValueError(
                'Superuser must be assigned to is_superuser=True.')

        return self.create_user(first_name, last_name, email, password, **other_fields)

    def create_user(self, first_name, last_name, email, password, **other_fields):
        if not email:
            raise ValueError(_('You must provide an email address'))

        email = self.normalize_email(email)
        user = self.model(first_name=first_name, last_name =last_name, email=email, **other_fields)
        user.set_password(password)
        user.save()
        return user


class Account(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(max_length=150, verbose_name='Ном')
    last_name = models.CharField(max_length=150, verbose_name='Насаб')
    email = models.EmailField(_('email'), unique=True)
    start_date = models.DateTimeField(default=timezone.now)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    objects = CustomAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', ]

    def __str__(self):
        return self.first_name + ' ' + self.last_name


class Profile(models.Model):
    GENDER_CHOICES = (
        ('М', 'Мард'),
        ('З', 'Зан'),
    )
    user = models.OneToOneField(Account,on_delete=models.CASCADE)
    image = models.ImageField(default='img/user.png', upload_to='images/user_images', verbose_name='Расм', null=True, blank=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, verbose_name='Ҷинс', null=True, blank=True)
    nationality = models.ForeignKey(Nationality, on_delete=models.CASCADE, verbose_name='Миллат', null=True, blank=True)
    education = models.ForeignKey(Education, on_delete=models.CASCADE, verbose_name='Маълумот', null=True, blank=True)
    phone = models.CharField(max_length=13, verbose_name='Телефон', null=True, blank=True)
    address = models.CharField(max_length=50, verbose_name='Адрес', null=True, blank=True)

    def __str__(self):
        return self.user.__str__()

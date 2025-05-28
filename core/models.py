from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.core.validators import RegexValidator


class AccountManager(BaseUserManager):
    def create_user(self, phone_number, password=None, **extra_fields):
        """
        Creates and saves a User with the given phone number and password.
        """
        if not phone_number:
            raise ValueError('Users must have a phone number')

        user = self.model(
            phone_number=phone_number,
            **extra_fields
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, phone_number, password=None, **extra_fields):
        """
        Creates and saves a superuser with the given phone number and password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(phone_number, password, **extra_fields)


class Account(AbstractBaseUser, PermissionsMixin):
    phone_regex = RegexValidator(
        regex=r'^\+?1?\d{9,15}$',
        message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed."
    )
    phone_number = models.CharField(
        validators=[phone_regex],
        max_length=17,
        unique=True,
        verbose_name='Phone Number'
    )

    # Required fields for custom user model
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)

    # Password fields (as requested)
    password = models.CharField(max_length=128, verbose_name='password')
    password2 = models.CharField(max_length=128, verbose_name='confirm password')

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = []

    objects = AccountManager()

    def __str__(self):
        return self.phone_number

    class Meta:
        verbose_name = 'Account'
        verbose_name_plural = 'Accounts'

class Profile(models.Model):
    account = models.OneToOneField(
        Account,
        on_delete=models.CASCADE,
        related_name='profile'
    )
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    email = models.EmailField(blank=True)
    birth_date = models.DateField(null=True, blank=True)
    bio = models.TextField(blank=True)

    def __str__(self):
        return f"Profile of {self.account.phone_number}"
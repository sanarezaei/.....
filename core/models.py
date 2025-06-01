from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.core.validators import RegexValidator
from django.conf import settings

class UserManager(BaseUserManager):
    def create_user(self, phone_number, password=None, password2=None, **extra_fields):
        if not phone_number:
            raise ValueError('Users must have a phone number')

        user = self.model(phone_number=phone_number, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, phone_number, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        extra_fields.pop('password2', None)

        if extra_fields.get('is_staff') is not True:
            raise ValueError("Superuser must have is_staff=True")
        if extra_fields.get('is_superuser') is not True:
            raise ValueError("Superuser must have is_superuser=True")

        return self.create_user(
            phone_number=phone_number,
            password=password,
            **extra_fields
        )


class User(AbstractBaseUser, PermissionsMixin):
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$')
    phone_number = models.CharField(
        validators=[phone_regex],
        max_length=17,
        unique=True,
    )
    password = models.CharField(max_length=128)
    password2 = models.CharField(max_length=128, blank=True, null=True)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.phone_number


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,\
                                verbose_name="profile")
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    bio = models.TextField()
    birth_date = models.DateField(null=True, blank=True)
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True,\
                               default='avatars/default.png')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.phone_number}'s Profile"
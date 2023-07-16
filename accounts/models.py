from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    gender = models.CharField(max_length=10)
    email = models.EmailField(primary_key=True)
    phone_number = models.CharField(max_length=20)

    USERNAME_FIELD = 'email'
    DEFAULT_PASSWORD = 'default'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'gender', 'phone_number']

from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import CustomUserManager

# Create your models here.
class User(AbstractUser):
    username = models.CharField(max_length=255, null=False, unique=True)
    password = models.CharField(max_length=255, null=False)
    phone_number = models.IntegerField(null=False)
    # rating = models.IntegerField()
    # image = models.ImageField(null=True, blank=True, upload_to="images/")

    objects = CustomUserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['password', 'phone_number']

    def __str__(self):
        return self.username

class Vendor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    long = models.CharField(max_length=255, null=True, blank=True)
    lat = models.CharField(max_length=255, null=True, blank=True)

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    email = models.EmailField(null=True, blank=True)

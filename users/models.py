import imp
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
from .managers import VendorManager
from .managers import CustomerManager

class Vendor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    username = models.CharField(max_length=255, null=False)
    password = models.CharField(max_length=255, null=False)
    phone_number = models.IntegerField(null=False)
    rating = models.IntegerField()
    image = models.ImageField(null=True, blank=True, upload_to="images/")
    long = models.CharField(max_length=255, null=True, blank=True)
    lat = models.CharField(max_length=255, null=True, blank=True)

    objects = VendorManager()

    def __str__(self):
        return self.user.username

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    phone_number = models.IntegerField(null=False)
    rating = models.IntegerField()
    image = models.ImageField(null=True, blank=True, upload_to="images/")
    email = models.EmailField(null=True, blank=True)

    objects = CustomerManager()

    def __str__(self):
        return self.user.username

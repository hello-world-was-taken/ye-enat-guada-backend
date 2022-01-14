from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    username = models.CharField(max_length=255, null=False)
    password = models.CharField(null=False)
    phone_number = models.IntegerField(null=False)
    rating = models.IntegerField()
    image = models.ImageField(null=True, blank=True, upload_to="images/")

class Vendor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    long = models.CharField()
    lat = models.CharField()

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    email = models.EmailField(null=True)

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
from .managers import CustomUserManager, VendorManager

# Create your models here.
class User(AbstractUser):
    username = models.CharField(max_length=255, null=False, unique=True)
    password = models.CharField(max_length=255, null=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['password']

    def __str__(self):
        return self.username

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

    # def save(self, username, password, phone_number, long, lat, rating, image, *args, **kwargs):
    #     self.user = username
    #     self.password = password

    #     user = User.objects.create(username=username, password=password)
        # self.user = user
        # self.password = password
        # self.phone_number = phone_number
        # self.long = long
        # self.lat = lat
        # self.rating = rating
        # self.image = image
        # vendor = Vendor.objects.create(user=user, phone_number=phone_number, rating=rating, long=long, lat=lat, image=image)

        # super().save(user=user, *args, **kwargs)

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    username = models.CharField(max_length=255, null=False, unique=True)
    password = models.CharField(max_length=255, null=False)
    phone_number = models.IntegerField(null=False)
    rating = models.IntegerField()
    image = models.ImageField(null=True, blank=True, upload_to="images/")
    email = models.EmailField(null=True, blank=True)

    # def save(self, username, password, phone_number, long, lat, rating, image, *args, **kwargs):
    #     self.user = username
    #     self.password = password

    #     user = User.objects.create(username=username, password=password)
    #     self.user = user
    #     self.password = password
    #     self.phone_number = phone_number
    #     self.long = long
    #     self.lat = lat
    #     self.rating = rating
    #     self.image = image

    #     super(Customer, self).save(*args, **kwargs)

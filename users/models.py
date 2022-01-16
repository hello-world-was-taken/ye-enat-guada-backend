from django.utils.translation import gettext_lazy as _
from statistics import mode
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model
from .managers import VendorManager
from .managers import CustomerManager, UserManager

class User(AbstractUser):
    class UserType(models.TextChoices):
        CUSTOMER = 'customer', _('Customer')
        VENDOR = 'vendor', _('Vendor')
        
    user_type = models.CharField(max_length=15, choices=UserType.choices, default=UserType.CUSTOMER,)
    objects = UserManager()

class Customer(models.Model):
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE, primary_key=True)
    phone_number = models.IntegerField(null=False)
    rating = models.IntegerField()
    image = models.ImageField(null=True, blank=True, upload_to="images/")
    email = models.EmailField(null=True, blank=True)

    objects = CustomerManager()

    def __str__(self):
        return self.user.username

class Vendor(models.Model):
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE, primary_key=True)
    username = models.CharField(max_length=255, null=False)
    password = models.CharField(max_length=255, null=False)
    phone_number = models.IntegerField(null=False)
    rating = models.IntegerField()
    image = models.ImageField(null=True, blank=True, upload_to="images/")
    long = models.CharField(max_length=255, null=True, blank=True)
    lat = models.CharField(max_length=255, null=True, blank=True)
    role = models.CharField(max_length=255)
    client = models.ManyToManyField(Customer)

    objects = VendorManager()

    def __str__(self):
        return self.user.username

class Order(models.Model):
    ordered_by = models.ForeignKey(Customer, related_name='ordered_by', on_delete=models.CASCADE)
    m_ordered = models.ForeignKey(Customer, related_name='m_ordered', on_delete=models.CASCADE) # the mother bet ordered
    orderd_on = models.TimeField(auto_now_add=True)
    ready = models.BooleanField(default=False)

class Client(models.Model):
    d_provider = models.ForeignKey(Customer, related_name='provider', on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, related_name='customer', on_delete=models.CASCADE) # the mother bet ordered

    def __str__(self):
        return f"orderd by: {self.ordered_by} ordered_mother_bet: {self.m_ordered} on: {self.orderd_on}"

class Dish(models.Model):
    d_provider = models.ForeignKey(get_user_model(), on_delete=models.CASCADE) # The mother bet with dish on the menu
    d_name = models.CharField(max_length=255, null=False, blank=False)
    d_price = models.FloatField(null=False, blank=False)

    def __str__(self):
        return f"{self.d_name} {self.d_provider}"
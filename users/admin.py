from dataclasses import fields
from multiprocessing import Manager
from operator import imod
from django.contrib import admin
from .models import Customer, Vendor, Dish, Order, User
# from .managers import UserManager

class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'first_name', 'last_name', 'id', 'username', 'user_type')

class CustomerAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone_number', 'rating', 'image')

class VendorAdmin(admin.ModelAdmin):
    fields=('username', 'phone_number', 'rating', 'image', 'long', 'lat')
    list_display = ('user', 'password', 'phone_number', 'rating', 'image')
admin.site.register(Customer, CustomerAdmin)
admin.site.register(Vendor, VendorAdmin)
admin.site.register(Dish)
admin.site.register(Order)
admin.site.register(User, UserAdmin)
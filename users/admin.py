from dataclasses import fields
from django.contrib import admin
from .models import Customer, Vendor
# from .models import User

# admin.site.register(User)

class CustomerAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone_number', 'rating', 'image')
    # fields=( 'phone_number', 'rating', 'image')

class VendorAdmin(admin.ModelAdmin):
    fields=('username', 'phone_number', 'rating', 'image', 'long', 'lat')
    list_display = ('user', 'password', 'phone_number', 'rating', 'image')
admin.site.register(Customer, CustomerAdmin)
admin.site.register(Vendor, VendorAdmin)
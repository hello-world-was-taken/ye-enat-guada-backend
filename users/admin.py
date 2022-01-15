from dataclasses import fields
from django.contrib import admin
from .models import Customer, Vendor, User

# Register your models here.
# admin.site.register(User)

# class UserInline(admin.StackedInline):
#     model = User
#     fields = ['username', 'password']

# class CustomerAdmin(admin.ModelAdmin):
#     inlines = [UserInline]

# class VendorAdmin(admin.ModelAdmin):
#     inlines = [UserInline]

# admin.site.unregister(User)
admin.site.register(Customer)
admin.site.register(Vendor)
admin.site.register(User)
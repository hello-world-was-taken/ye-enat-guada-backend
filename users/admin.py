from django.contrib import admin
from .models import Customer, User, Vendor

# Register your models here.
admin.site.register(User)
admin.site.register(Vendor)
admin.site.register(Customer)

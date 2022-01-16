from lib2to3.pytree import Base
from tkinter import E
from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import BaseUserManager

class UserManager(BaseUserManager):
    def create_user(self, username, first_name, last_name, password, email=None, **extra_fields):
        """
        Create and save a User with the given email and password.
        """
        if not username:
            raise ValueError(_('The Username must be set'))
        v_user = self.model(username=username, first_name=first_name, last_name=last_name, email=email, **extra_fields)
        v_user.set_password(password)
        v_user.user_type = v_user.UserType.CUSTOMER
        v_user.save()
        return v_user

    def create_superuser(self, username, password, first_name="admin", last_name="admin", **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))
        return self.create_user(username=username, password=password, first_name=first_name, last_name=last_name, **extra_fields)

class VendorManager(models.Manager):
    def create_user(self, user, phone_number, rating, long, lat, image=None, **extra_fields):
        """
        Create and save a User with the given email and password.
        """
        if not user:
            raise ValueError(_('The Username must be set'))
        v_user = self.model(user=user, phone_number=phone_number, rating=rating, image=image, long=long, lat=lat, **extra_fields)
        v_user.user.user_type = v_user.user.UserType.VENDOR
        v_user.user.save()
        v_user.save()
        return v_user

class CustomerManager(models.Manager):
    def create_user(self, user, phone_number, rating, image=None, email=None, **extra_fields):
        """
        Create and save a User with the given email and password.
        """
        if not user:
            raise ValueError(_('The Username must be set'))
        c_user = self.model(user=user, phone_number=phone_number, rating=rating, image=image, email=email, **extra_fields)
        c_user.save()
        return c_user


# Tired of typing this out
# Vendor.objects.create_user(username="a", password="b", phone_number=456, rating=5, image=None, long=4, lat=4)
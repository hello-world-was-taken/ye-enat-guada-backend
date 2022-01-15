from django.contrib.auth.base_user import BaseUserManager
# from django.utils.translation import ugettext_lazy as _
# from .models import User
from django.db import models
from django.contrib.auth import get_user_model
# User = get_user_model()


class CustomUserManager(BaseUserManager):
    """
    Custom user model manager where email is the unique identifiers
    for authentication instead of usernames.
    """
    def create_user(self, username, password, **extra_fields):
        """
        Create and save a User with the given email and password.
        """
        if not username:
            raise ValueError(_('The Username must be set'))
        # username = self.normalize_???(username)
        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, username, password, **extra_fields):
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
        return self.create_user(username, password, **extra_fields)


class VendorManager(models.Manager):
    def create_user(self, username, password, phone_number, rating, long, lat, image=None, **extra_fields):
        """
        Create and save a User with the given email and password.
        """
        if not username:
            raise ValueError(_('The Username must be set'))
        # username = self.normalize_???(username)
        user= get_user_model().objects.create_user(username=username, password=password)
        v_user = self.model(user=user, phone_number=phone_number, rating=rating, image=image, long=long, lat=lat, **extra_fields)
        # user.set_password(password)
        v_user.save()
        return v_user


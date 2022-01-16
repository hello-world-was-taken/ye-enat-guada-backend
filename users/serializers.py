from urllib import request
from rest_framework import serializers
from .models import Vendor, Customer, Dish, Order
from django.contrib.auth import get_user_model
from drf_extra_fields.fields import Base64ImageField
import json


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('id', 'username', 'user_type', 'first_name', 'last_name', 'email')


class VendorSerializer(serializers.ModelSerializer):
    user = UserSerializer(many=False, required=False) # to get around the {'user':'this field is required'} error
    class Meta:
        model = Vendor
        fields = ['user', 'phone_number', 'image', 'rating', 'long', 'lat']

    def create(self, validated_data):
        validated_data.update(self.context)
        image = validated_data.pop('image')
        user = validated_data.pop('user')

        user = json.loads(user)

        c_user = get_user_model().objects.create_user(**user)
        c_user.user_type = c_user.UserType.VENDOR
        # c_user.save()
        
        return Vendor.objects.create_user(user=c_user, image=image, **validated_data)


class CustomerSerializer(serializers.ModelSerializer):
    user = UserSerializer(many=False, required=False)
    class Meta:
        model = Customer
        fields = ('user', 'phone_number', 'rating', 'image')

    def create(self, validated_data):
        validated_data.update(self.context)
        image = validated_data.pop('image')
        user = validated_data.pop('user') # work around NEEDS A BETTER SOLUTION
        user = json.loads(user) # changes the string to a dictionary
        c_user = get_user_model().objects.create_user(**user)
        c_user.user_type = c_user.UserType.CUSTOMER

        return Customer.objects.create_user(user=c_user, image=image, **validated_data)


# class UserChildSerializer(serializers.ModelSerializer):
#     user = UserSerializer(many=True)
#     class Meta:
#         model = Customer
#         fields = ('user', 'phone_number', 'rating', 'image')

class DishSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dish
        fields = ('d_name', 'd_price', 'd_provider')

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ('ordered_by', 'm_ordered', 'orderd_on', 'ready')
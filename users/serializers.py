from urllib import request
from rest_framework import serializers
from .models import Vendor, Customer
from django.contrib.auth.models import User
from drf_extra_fields.fields import Base64ImageField
import json


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username')


class VendorSerializer(serializers.ModelSerializer):
    user = UserSerializer(many=False, required=False) # to get around the {'user':'this field is required'} error
    class Meta:
        model = Vendor
        fields = ['user', 'phone_number', 'image', 'rating', 'long', 'lat']

    def create(self, validated_data):
        # print(validated_data)
        validated_data.update(self.context)
        image = validated_data.pop('image')
        user = validated_data.pop('user')

        user = json.loads(user)

        c_user = User.objects.create_user(**user)
        return Vendor.objects.create_user(user=c_user, image=image, **validated_data)


class CustomerSerializer(serializers.ModelSerializer):
    # print("haaaaaaaaaaaaaaaaaaaaaaaaa")
    user = UserSerializer(many=False, required=False)
    class Meta:
        model = Customer
        fields = ('user', 'phone_number', 'rating', 'image')

    def create(self, validated_data):
        # print("type: ", type(validated_data))
        # print(self.context)
        validated_data.update(self.context)
        # print(res)
        image = validated_data.pop('image')
        user = validated_data.pop('user') # work around NEEDS A BETTER SOLUTION
        # print(user)
        user = json.loads(user) # changes the string to a dictionary
        # print(type(user))
        # print("\n")
        # print("\n")
        
        # for user_data in user:
        c_user = User.objects.create_user(**user)

        return Customer.objects.create_user(user=c_user, image=image, **validated_data)


class UserChildSerializer(serializers.ModelSerializer):
    # username = serializers.CharField(max_length=255, null=False)
    # password = serializers.CharField(max_length=255, null=False)
    # phone_number = serializers.IntegerField(null=False)
    # rating = serializers.IntegerField()
    # image = serializers.ImageField(null=True, blank=True, upload_to="images/")
    # email = serializers.EmailField(null=True, blank=True)
    user = UserSerializer(many=True)
    class Meta:
        model = Customer
        fields = ('user', 'phone_number', 'rating', 'image')
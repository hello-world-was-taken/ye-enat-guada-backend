from rest_framework import serializers
from .models import Vendor, Customer
from django.contrib.auth.models import User
from drf_extra_fields.fields import Base64ImageField

class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = ('id', 'username', 'password')

class VendorSerializer(serializers.ModelSerializer):
  # user = UserSerializer(many=False)
  class Meta:
    model = Vendor
    fields = ['username', 'phone_number', 'image', 'password', 'rating', 'long', 'lat']
  
  def create(self, validated_data):
    image=validated_data.pop('image')

    return Vendor.objects.create_user(image=image, **validated_data)

class CustomerSerializer(serializers.ModelSerializer):
    # user = UserSerializer(many=True)
    class Meta:
      model = Customer
      fields = ('username', 'password', 'phone_number', 'rating', 'image')

    def create(self, validated_data):
      image=validated_data.pop('image')

      return Customer.objects.create_user(image=image, **validated_data)
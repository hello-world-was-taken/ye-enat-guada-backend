from rest_framework import serializers
from .models import Vendor, Customer
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
      model = User
      fields = ('id', 'username', 'password')

class VendorSerializer(serializers.ModelSerializer):
    user = UserSerializer(many=True)
    class Meta:
      model = Vendor
      fields = ('username', 'phone_number', 'rating', 'long', 'lat')

class CustomerSerializer(serializers.ModelSerializer):
    user = UserSerializer(many=True)
    class Meta:
      model = Customer
      fields = ('username', 'phone_number', 'rating')
      
# class ArtistSerializer(serialisers.ModelSerializer):
#   songs = SongSerializer(many=True)
from rest_framework import serializers
from .models import Vendor, Customer
from django.contrib.auth.models import User
from drf_extra_fields.fields import Base64ImageField

class UserSerializer(serializers.ModelSerializer):
    class Meta:
      model = User
      fields = ('id', 'username', 'password')

class VendorSerializer(serializers.ModelSerializer):
    # user = UserSerializer(many=True)
    # image = Base64ImageField(
    #     max_length=None, use_url=True,
    # )
    # image=Base64ImageField()
    class Meta:
      model = Vendor
      fields = ['username', 'phone_number', 'image', 'password', 'rating', 'long', 'lat']
    #   exclude = ['image']
    
    def create(self, validated_data):
      # image_file = validated_data.pop("image", None)
      # if image_file != None:
        # img = open(image_file, 'rb')
        # validated_data.append(img)
      image=validated_data.pop('image')

      return Vendor.objects.create_user(image=image, **validated_data)

class CustomerSerializer(serializers.ModelSerializer):
    user = UserSerializer(many=True)
    class Meta:
      model = Customer
      fields = ('username', 'phone_number', 'rating')
      
# class ArtistSerializer(serialisers.ModelSerializer):
#   songs = SongSerializer(many=True)
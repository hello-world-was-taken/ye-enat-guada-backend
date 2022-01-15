from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.shortcuts import render
from .models import Customer, Vendor
from django.contrib.auth.models import User
from .serializers import CustomerSerializer, UserSerializer, VendorSerializer
from rest_framework.parsers import JSONParser, MultiPartParser
from django.http.response import JsonResponse
from rest_framework.views import APIView
from rest_framework.exceptions import AuthenticationFailed

class RegisterVendor(APIView):
    parser_classes = (MultiPartParser, )

    def post(self, request, format=None):
        print(request.data)
        print("\n\n\n")
        serializer = VendorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

class RegisterCustomer(APIView):
    parser_classes = (MultiPartParser, )

    def post(self, request, format=None):
        print(request.data)
        print("\n\n\n")
        serializer = CustomerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)



        
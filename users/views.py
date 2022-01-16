from sqlite3 import converters
from telnetlib import STATUS
from urllib import response
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.shortcuts import render
from .models import Customer, Vendor, Dish
from django.contrib.auth.models import User
from .serializers import CustomerSerializer, UserSerializer, VendorSerializer, UserChildSerializer, DishSerializer
from rest_framework.parsers import JSONParser, MultiPartParser, FormParser
from django.http.response import JsonResponse
from rest_framework.views import APIView
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.response import Response
import datetime, jwt
from rest_framework.decorators import api_view
import json
from rest_framework.permissions import IsAuthenticated

class RegisterVendor(APIView):
    parser_classes = (MultiPartParser, )

    def post(self, request, format=None):
        user = request.data.get("user")
        dic = {}
        dic['user'] = user
        serializer = VendorSerializer(data=request.data, context=dic)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=200)
        return JsonResponse(serializer.errors, status=400)

class RegisterCustomer(APIView):
    parser_classes = (MultiPartParser, FormParser, JSONParser)

    def post(self, request, format=None):
        user = request.data.get("user")
        dic = {}
        dic['user'] = user
        serializer = CustomerSerializer(data=request.data, context=dic)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=200)
        return JsonResponse(serializer.errors, status=400)

class GetUserData(APIView):
    permission_classes = [IsAuthenticated]
    parser_classes = (MultiPartParser,)

    def get(self, request):
        user = request.user
        if request.user.user_type == 'customer':
            customer = Customer.objects.filter(user=user).first()
            serializer = CustomerSerializer(customer)
        else:
            vendor = Vendor.objects.filter(user=user).first()
            serializer = VendorSerializer(vendor)
        return JsonResponse(serializer.data)

class AddDish(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = DishSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=200)
        return JsonResponse(serializer.errors, status=400)
    def put(self, request):
        d_id = request.data['d_id']
        d_exists = Dish.objects.get(id=d_id)
        if not d_exists:
            return JsonResponse("Dish Doesn't Exits", status=400, safe=False)
        serializer = DishSerializer(d_exists, data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=200)
        return JsonResponse(serializer.errors, status=400)

    
    def delete(self, request):
        d_id = request.data['d_id']
        if not d_id:
            return JsonResponse("Dish Doesn't Exits", status=400, safe=False)
        Dish.objects.get(id=d_id).delete()
    
        return JsonResponse("Dish has been successfully removed!", status=200)
        

class Dummy(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return HttpResponse("<h1>BISRAT HAS A HASTY ATTITUDE. CHILL BRUH!</h2>")

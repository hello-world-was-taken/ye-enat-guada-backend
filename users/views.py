from sqlite3 import converters
from urllib import response
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.shortcuts import render
from .models import Customer, Vendor
from django.contrib.auth.models import User
from .serializers import CustomerSerializer, UserSerializer, VendorSerializer, UserChildSerializer
from rest_framework.parsers import JSONParser, MultiPartParser, FormParser
from django.http.response import JsonResponse
from rest_framework.views import APIView
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.response import Response
import datetime, jwt
from rest_framework.decorators import api_view
import json

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
    parser_classes = (MultiPartParser, FormParser, JSONParser)

    def post(self, request, format=None):
        print(request.data)
        # print("\n\n\n")
        # user = request.data.get("user")
        # phone_number = request.data.get("phone_number")
        # image = request.data.get("image")
        # print(user, phone_number, image)
        # print(request.data)
        # request.data["user"]= user
        # print(request.data)
        # converted = json.dumps(request.data) 
        # print(request.FILES)
        # print(converted)
        # dic= []
        # list_keys = list(request.data.keys())
        # print(list_keys)
        # for i in range(len(list_keys)):
        #     print(i)
        #     if list_keys[i] == 'image':
        #         dic[list_keys[i]]=request.FILES
        #         continue
        #     dic[list_keys[i]]=request.data[list_keys[i]]
        # print(dic)
        user = request.data.get("user")
        print(user)
        print(request.data)
        dic = {}
        dic['user'] = user
        print(dic)
        serializer = CustomerSerializer(data=request.data, context=dic)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

class GetUserData(APIView):
    parser_classes = (MultiPartParser,)

    def get(self, request, username):
        data = User.objects.filter(username=username).first()
        customer = Customer.objects.filter(user=data)
        print(customer)
        # print(data)
        # print("\n\n\n")
        # print("\n\n\n")
        # print("\n\n\n")
        serializer = UserChildSerializer(customer)
        # if serializer.is_valid():
        return JsonResponse(serializer.data)
        # return JsonResponse(serializer.errors, status=500)

@csrf_exempt
@api_view(['POST'])
def login(request):
    if request.method == 'POST':
        # print(request.data)
        username = request.data['username']
        password = request.data['password']

        user = User.objects.filter(username=username).first()

        if user is None:
            return JsonResponse('User is not Registered!', safe=False)
        if not user.check_password(password):
            return JsonResponse('Incorrect username or password!', safe=False)

        payload = {
            'id': user.id,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=1),
            'iat': datetime.datetime.utcnow()
        }

        token = jwt.encode(payload, 'secret', algorithm='HS256')

        response = Response()
        response.data = {'jwt':token}
        # response.set_cookie(key='jwt', value=token, httponly=True)
        return JsonResponse({'jwt':token})
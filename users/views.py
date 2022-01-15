from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.shortcuts import render
from .models import Customer, Vendor
from django.contrib.auth.models import User
from .serializers import CustomerSerializer, UserSerializer, VendorSerializer
from rest_framework.parsers import JSONParser, MultiPartParser
from django.http.response import JsonResponse
from rest_framework.views import APIView

# Create your views here.


# def fun(request, username, password):
#     user = User.objects.all().filter(username=username).first()
#     cus = Customer.objects.all().filter(user=user).first()
#     ven = Vendor.objects.all().filter(user=user).first()

#     if cus != None:
#         return HttpResponse(f'it is a customer name: {cus} rating: {cus.rating} image: {cus.image}')
#     elif ven != None:
#         return HttpResponse(f'it is a vendor name: {ven} rating: {ven.rating} image: <img src="{ven.image}"/>')
#     else:
#         print("not a valid user")

# @csrf_exempt
# def register_vendor(request):
#     if request.method == 'POST':
#         # user_data = JSONParser().parse(request)

#         ven_serializer = VendorSerializer(data=JSONParser().parse(request))
#         ven_serializer.is_valid(raise_exception=True)
#         ven_serializer.save()

#         return JsonResponse('User created successfully!', safe=False)

class UserUploadedPicture(APIView):
    parser_classes = (MultiPartParser, )

    def post(self, request, format=None):
        print(request.data)
        print("\n\n\n")
        serializer = VendorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)
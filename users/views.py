from django.http import HttpResponse
from django.shortcuts import render
from .models import Customer, Vendor
from django.contrib.auth.models import User

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

def register(request):
    if request.method == 'POST':
            
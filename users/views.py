from .models import Customer, Vendor, Dish, Order
from django.contrib.auth import get_user_model
from .serializers import CustomerSerializer, VendorSerializer, DishSerializer, OrderSerializer
from rest_framework.parsers import JSONParser, MultiPartParser, FormParser
from django.http.response import JsonResponse
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated


# Register as Vendor - Mother bet owner
class RegisterVendor(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request, format=None):
        user = request.data.get("user")
        dic = {}
        dic['user'] = user
        serializer = VendorSerializer(data=request.data, context=dic)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=200)
        return JsonResponse(serializer.errors, status=400)


# Register as Customer
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


# Delete the account of the user whom is verified through token
class DeleteAccount(APIView):
    permission_classes = [IsAuthenticated]
    parser_classes = (MultiPartParser, FormParser, JSONParser)

    def post(self, request, format=None):
        u_id = request.user.id
        get_user_model().objects.filter(id=u_id).first().delete()
        return JsonResponse("The user has been successfully deleted!", safe=False)


# Return Data related to a certain user whom is verified via token
class GetUserData(APIView):
    permission_classes = [IsAuthenticated]
    parser_classes = (MultiPartParser,)

    def get(self, request):
        user = request.user
        print(request.user.user_type)
        if request.user.user_type == 'customer':
            customer = Customer.objects.filter(user=user).first()
            serializer = CustomerSerializer(customer)
        elif request.user.user_type == 'vendor':
            vendor = Vendor.objects.filter(user=user).first()
            serializer = VendorSerializer(vendor)
        return JsonResponse(serializer.data)


class DishView(APIView):
    permission_classes = [IsAuthenticated]

    # Add Dishes to your menu if you own are a Mother bet
    def post(self, request):
        print(request.user.user_type)
        if request.user.user_type == 'customer':
            return JsonResponse("You are not a vendor", status=400, safe=False)
        serializer = DishSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=200)
        return JsonResponse(serializer.errors, status=400)

    # Update you specific Dishes if you own a Mother bet
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

    # Remove Dishes from you menu if you are a Mother bet
    def delete(self, request):
        d_id = request.data['d_id']
        if not d_id:
            return JsonResponse("Dish Doesn't Exits", status=400, safe=False)
        Dish.objects.get(id=d_id).delete()
        return JsonResponse("Dish has been successfully removed!", status=200)

    # Get menu of the specified Mother bet
    def get(self, request):
        # here the d_provider is for the owner's of the Mother bet
        d_provider = request.data['d_provider']
        u = get_user_model().objects.get(id=d_provider)
        dish_list = Dish.objects.all().filter(d_provider=u)
        dish = DishSerializer(dish_list, many=True)
        return JsonResponse(dish.data, status=200, safe=False)


class OrderView(APIView):
    permission_classes = [IsAuthenticated]

    # Allows user to order
    def post(self, request):
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=200)
        return JsonResponse(serializer.errors, status=400)

    # Allows vendors to update if a food is ready or not. Customer doesn't have the priviledge to do so.
    def put(self, request):
        if not request.user.user_type == 'vendor':
            return JsonResponse("You are not a vendor", status=400, safe=False)
        order_id = request.data['id']
        current_order = Order.objects.filter(order_id=id).first()

        if not (request.user.id == Dish.objects.get(id=order_id).m_ordered.id):
            return JsonResponse("You are not the mother be ordered!", status=400, safe=False)
        serializer = OrderSerializer(current_order, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=200)
        return JsonResponse(serializer.errors, status=400)

    # IF UNFORSEEN EVENTS OCCUR, THE MOTHER BET WILL BE ALLOWED TO GO BACK ON THE CONTRACT

    # Return the amount of order prior.
    def get(self, request):
        # here the d_provider is for the owner's of the Mother bet
        mother_bet_id = request.data['mother_bet']
        u = Order.objects.get(m_ordered=mother_bet_id)
        order = OrderSerializer(u, many=True)
        return JsonResponse(order.data, status=200, safe=False)

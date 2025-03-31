from rest_framework_simplejwt.token_blacklist.models import BlacklistedToken, OutstandingToken
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import IsAuthenticated, IsAdminUser 
from rest_framework.response import Response
from .serializers import RegisterSerializer
from django.contrib.auth.models import User
from rest_framework.views import APIView
from django.shortcuts import render
from rest_framework import status, serializers
from apps.order.models import Order
from apps.order.serializers import OrderSerializer
# Create your views here.

class RegisterView(TokenObtainPairView):
    serializer_class = RegisterSerializer

class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        tokens = OutstandingToken.objects.filter(user=request.user)
        for token in tokens:
            BlacklistedToken.objects.get_or_create(token=token)
        return Response({"message": "Log out!!!!"})


class ProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        user = request.user
        user_data = {
            "username": user.username,
            "email": user.email,
        }
        return Response(user_data)

class ProfileUpdateView(APIView):
    permission_classes = [IsAuthenticated]

    def put(self, request, *args, **kwargs):
        user = request.user
        serializer = RegisterSerializer(user, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ListUserView(APIView):
    permission_classes = [IsAdminUser]

    def get(self, request):
        users = User.objects.all() 
        usernames = [user.username for user in users]
        return Response(usernames, status=status.HTTP_200_OK)

class DeleteUserView(APIView):
    permission_classes = [IsAdminUser]

    def delete(self, request, id):
        user = User.objects.get(id=id)
        user.delete() 
        return Response({"message": "User deleted successfully."}, status=status.HTTP_204_NO_CONTENT)

class OrderListView(APIView):
    permission_classes = [IsAdminUser]  

    def get(self, request):
        orders = Order.objects.all()  
        serializer = OrderSerializer(orders, many=True) 
        return Response(serializer.data, status=status.HTTP_200_OK)

class StatsView(APIView):
    permission_classes = [IsAdminUser]

    def get(self, request):
        total_orders = Order.objects.count()
        total_students = Student.objects.count()
        stats = {
            'total_orders': total_orders,
            'total_students': total_students,
        }
        return Response(stats, status=status.HTTP_200_OK)

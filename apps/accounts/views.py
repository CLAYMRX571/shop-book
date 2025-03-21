from rest_framework_simplejwt.token_blacklist.models import BlacklistedToken, OutstandingToken
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .serializers import RegisterSerializer
from rest_framework.views import APIView
from django.shortcuts import render
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
        user_data = {
            "username": user.username,
            "email": user.email,
        }
        return Response(user_data)

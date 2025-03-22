from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import Wishlist
from apps.books.models import Book
from django.contrib.auth.models import User
from .serializers import WishlistSerializer

class WishlistAddView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        book_id = request.data.get('book_id')
        user = request.data.get('user')
        wishlist = Wishlist.objects.create(user=user, book_id=book_id)
        serializer = WishlistSerializer(wishlist)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class WishlistView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        user = request.query_params.get('user')
        wishlists = Wishlist.objects.filter(user=user)
        serializer = WishlistSerializer(wishlists, many=True) 
        return Response(serializer.data, status=status.HTTP_200_OK)

class WishlistDeleteView(APIView):
    def delete(self, request, id):
        wishlists = Wishlist.objects.get(id=id)
        wishlists.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
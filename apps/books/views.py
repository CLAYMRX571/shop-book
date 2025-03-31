from .serializers import BookSerializer, BookSearchSerializer
from rest_framework.permissions import AllowAny, IsAdminUser
from rest_framework.views import APIView, View
from rest_framework.response import Response
from django.http import JsonResponse
from django.shortcuts import render
from rest_framework import status
from .models import Book
from .paginations import MyCursorPagination 

class BookAllView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        books = Book.objects.all()
        serializers = BookSerializer(books, many=True)
        pagination_class = MyCursorPagination
        return Response(serializers.data)

class BookCreateView(APIView):
    permission_classes = [IsAdminUser]

    def post(self, request):
        serializer = BookSerializer(data=request.data)  
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class BookDetailView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, id):
        book = Book.objects.get(id=id)
        serializer = BookSerializer(book)
        return Response(serializer.data)

class BookUpdateView(APIView):
    permission_classes = [IsAdminUser]

    def put(self, request, id):
        book = Book.objects.get(id=id)  
        serializer = BookSerializer(book, data=request.data) 
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        return Response(serializer.errors, status=400)

class BookDeleteView(APIView):
    permission_classes = [IsAdminUser]

    def delete(self, request, id):
        book = Book.objects.get(id=id)
        book.delete()
        return Response(status=204)

class BookSearchView(View):
    def get(self, request, slug=None):
        query = request.GET.get('search', '')
        books = Book.objects.filter(name__icontains=query) | Book.objects.filter(author__icontains=query)
        serializer = BookSearchSerializer(books, many=True)
        return JsonResponse(serializer.data, safe=False)
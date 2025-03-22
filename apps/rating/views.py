from .serializers import ReviewSerializer, DetailSerializer, RatingSerializer
from rest_framework.permissions import IsAdminUser, AllowAny
from .models import Book, Review, Rating, Reviews
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import render
from rest_framework import status
from django.db.models import Avg

class BookReviewsView(APIView):
    def post(self, request, id):
        book = Book.objects.get(id=id)
        serializer = ReviewSerializer(data=request.data)
        if serializer.is_valid():
            review = serializer.save(book=book, user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class BookRateView(APIView):
    def post(self, request, id):
        book = Book.objects.get(id=id)
        serializer = RatingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user, book=book)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ReviewDetailView(APIView):
    def get(self, request, id):
        book = Book.objects.get(id=id)
        reviews = book.reviews.all()
        serializer = DetailSerializer(reviews, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class ReviewDeleteView(APIView):
    permission_classes = [IsAdminUser]

    def delete(self, request, id):
        review = Review.objects.get(id=id)
        review.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class TopReviewView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        books = Book.objects.annotate(average_rating=Avg('ratings__rating')).order_by('-average_rating')[:10]
        serialized_books = [
            {
                "id": book.id,
                "name": book.name,  
                "author": book.author,
                "average_rating": book.average_rating
            } for book in books
        ]
        return Response(serialized_books, status=status.HTTP_200_OK)
from rest_framework import serializers
from .models import Book

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'name', 'author', 'price', 'date', 'photo', 'description']

class BookSearchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'price', 'date', 'photo', 'description']
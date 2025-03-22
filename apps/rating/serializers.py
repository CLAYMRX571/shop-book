from rest_framework import serializers
from .models import Review, Rating, Reviews

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['rating', 'comment']

class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ['book', 'rating']

class DetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reviews
        fields = ['user', 'content', 'created_at']
        read_only_fields = ['user', 'created_at']
    
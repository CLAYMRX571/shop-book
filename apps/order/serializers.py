from rest_framework import serializers
from .models import Order, ChangeStatus, History

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'

class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChangeStatus
        fields = ['status']

class HistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = History
        fields = ['id', 'order_date', 'total_price', 'status']
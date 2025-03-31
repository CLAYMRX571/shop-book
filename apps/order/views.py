from .serializers import OrderSerializer, StatusSerializer, HistorySerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import status
from .models import Order, ChangeStatus, History

class OrderCreateView(APIView):
    def post(self, request):
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            order = serializer.save()
            return Response(OrderSerializer(order).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class OrderView(generics.ListAPIView):
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)

class DetailView(generics.RetrieveAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        obj = self.get_object()
        serializer = self.get_serializer(obj)
        return Response(serializer.data, status=status.HTTP_200_OK)

class CancelView(APIView):
    permission_classes = [IsAuthenticated]

    def put(self, request, id):
        order = Order.objects.get(id=id, user=request.user)
        order.status = 'canceled'
        order.save()
        serializer = OrderSerializer(order)
        return Response(serializer.data, status=status.HTTP_200_OK)

class ChangeStatusView(APIView):
    def put(self, request, id):
        status = changestatus.objects.get(id=id)
        serializer = StatusSerializer(status, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class HistoryView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        orders = Order.objects.filter(user=request.user).order_by('-created_at')
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data)
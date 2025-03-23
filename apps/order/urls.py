from django.urls import path
from apps.order.views import OrderCreateView, OrderView, DetailView, CancelView, ChangeStatusView, HistoryView

urlpatterns = [
    path('create/', OrderCreateView.as_view(), name='create'),
    path('all/', OrderView.as_view(), name='all'),
    path('detail/<int:pk>/', DetailView.as_view(), name='detail'),  
    path('cancel/<int:id>/', CancelView.as_view(), name='cancel'),
    path('change/<int:id>/', ChangeStatusView.as_view(), name='change'),
    path('history/', HistoryView.as_view(), name='history'),
]
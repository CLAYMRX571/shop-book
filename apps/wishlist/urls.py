from django.urls import path
from apps.wishlist.views import WishlistAddView, WishlistView, WishlistDeleteView

urlpatterns = [
    path('add/', WishlistAddView.as_view(), name='add'),
    path('view/', WishlistView.as_view(), name='view'),
    path('delete/<int:id>/', WishlistDeleteView.as_view(), name='delete'),
]
from django.urls import path
from .views import BookReviewsView, BookRateView, ReviewDetailView, ReviewDeleteView, TopReviewView

urlpatterns = [
    path('reviews/<int:id>/', BookReviewsView.as_view(), name='reviews'),
    path('rate/<int:id>/', BookRateView.as_view(), name='rate'),
    path('detail/<int:id>/', ReviewDetailView.as_view(), name='detail'),
    path('delete/<int:id>/', ReviewDeleteView.as_view(), name='delete'),
    path('top/', TopReviewView.as_view(), name='top'),
]
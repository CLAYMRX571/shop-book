from django.urls import path
from apps.books.views import BookAllView, BookCreateView, BookDetailView, BookUpdateView, BookDeleteView, BookSearchView

urlpatterns = [
    path('all/', BookAllView.as_view(), name='all'),
    path('create/', BookCreateView.as_view(), name='create'),
    path('book/<int:id>/', BookDetailView.as_view(), name='book'),
    path('update/<int:id>/', BookUpdateView.as_view(), name='update'),
    path('delete/<int:id>/', BookDeleteView.as_view(), name='delete'),
    path('search/<slug:slug>/', BookSearchView.as_view(), name='search'),
]
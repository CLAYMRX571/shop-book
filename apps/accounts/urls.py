from django.urls import path
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
)
from apps.accounts.views import RegisterView, LogoutView, ProfileView, ProfileUpdateView, ListUserView, DeleteUserView, OrderListView, StatsView

schema_view = get_schema_view(
    openapi.Info(
        title="Rest Api",
        default_version='v1',
        description="API",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="claymrx571@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]

urlpatterns += [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', TokenObtainPairView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('profile/update/', ProfileUpdateView.as_view(), name='update'),
]

urlpatterns += [
    path('list/', ListUserView.as_view(), name='list'),
    path('delete/<int:id>/', DeleteUserView.as_view(), name='delete'),
    path('orders/', OrderListView.as_view(), name='order'),
    path('stats/', StatsView.as_view(), name='stats'),
]

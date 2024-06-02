from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
urlpatterns = [
    path('token/', include("accounts.api.v1.urls.jwt_urls")),
    path('', include("accounts.api.v1.urls.user_urls")),
]
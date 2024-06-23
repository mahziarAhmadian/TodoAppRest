from django.urls import path, include

from ..views import user_views

app_name = "api-v1"
urlpatterns = [
    path('login/',
         user_views.UserLoginGenericAPIView.as_view(),
         name='login'),

    path('register/',
         user_views.UserRegistrationCreateAPIView.as_view(),
         name='register'),

    path('password_reset/',
         user_views.PasswordResetUpdateAPIView.as_view(),
         name='password_reset'),

]

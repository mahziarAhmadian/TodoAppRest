from django.urls import path, include

from ..views import user_views

urlpatterns = [
    # path('', include('djoser.urls')),
    path('login/',
         user_views.UserLoginGenericAPIView.as_view(),
         name='login'),

    path('register/',
         user_views.UserRegistrationCreateAPIView.as_view(),
         name='register'),

    path('password_reset/',
         user_views.PasswordResetUpdateAPIView.as_view(),
         name='password_change'),
    #
    # path('^/reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/',
    #     user_views.PasswordResetConfirmView.as_view(),
    #     name='password_reset_confirm'),
    #
    # path('/user-profile/',
    #     user_views.UserProfileAPIView.as_view(),
    #     name='user_profile'),

]

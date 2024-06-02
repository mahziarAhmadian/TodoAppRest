from django.contrib.auth import get_user_model
from django.contrib.sites.shortcuts import get_current_site
from rest_framework import generics, permissions, status, views
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response
from accounts.models import User
from ..serializers import user_serializers
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token

User = get_user_model()


class UserRegistrationCreateAPIView(generics.CreateAPIView):
    """
    Endpoint for user registration.

    """

    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = user_serializers.UserRegistrationSerializer
    queryset = User.objects.all()


class UserLoginGenericAPIView(generics.GenericAPIView):
    """
    Endpoint for user login. Returns authentication token on success.

    """

    permission_classes = (permissions.AllowAny,)
    serializer_class = user_serializers.UserLoginSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#
#
class PasswordResetUpdateAPIView(generics.UpdateAPIView):
    """
    Endpoint to reset  user  password .
    """

    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = user_serializers.PasswordResetSerializer

    def get_object(self):
        return self.request.user

    def update(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            user = self.get_object()
            if user.check_password(serializer.validated_data['old_password']):
                user.set_password(serializer.validated_data['new_password'])
                user.save()
                return Response({'message': 'Password updated successfully'}, status=status.HTTP_200_OK)
            else:
                return Response({'error': 'Incorrect old password'}, status=status.HTTP_400_BAD_REQUEST)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#
#     def get_user_profile(self, email):
#         try:
#             user_profile = UserProfile.objects.get(user__email=email)
#         except:
#             return None
#         return user_profile
#
#
# class PasswordResetConfirmView(views.APIView):
#     """
#     Endpoint to change user password.
#
#     """
#
#     permission_classes = (permissions.AllowAny, )
#     serializer_class = serializers.PasswordResetConfirmSerializer
#
#     def post(self, request, *args, **kwargs):
#
#         serializer = self.serializer_class(
#             data=request.data,
#             context={
#                 'uidb64': kwargs['uidb64'],
#                 'token': kwargs['token']
#             })
#
#         if serializer.is_valid(raise_exception=True):
#             new_password = serializer.validated_data.get('new_password')
#             user = serializer.user
#             user.set_password(new_password)
#             user.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
#
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#
# class UserProfileAPIView(generics.RetrieveAPIView):
#     """
#     Endpoint to retrieve user profile.
#
#     """
#
#     permission_classes = (permissions.IsAuthenticated, )
#     authentication_classes = (TokenAuthentication, )
#     serializer_class = serializers.UserProfileSerializer
#
#     def get_object(self):
#         return self.request.user.userprofile

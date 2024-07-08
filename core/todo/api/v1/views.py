import requests
from .serializers import TaskSerializer
from ...models import Task
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import generics
from rest_framework.response import Response
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page


class TaskModelViewSet(viewsets.ModelViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = TaskSerializer
    queryset = Task.objects.all()


class WeatherGenericAPIView(generics.RetrieveAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = None  # Update this with the appropriate serializer class if needed

    def get_weather_information_open_weather(self):
        try:
            response = requests.get(
                "https://api.openweathermap.org/data/2.5/weather?lat=35.7050249&lon=51.4757335&APPID=5f4ed15e4c9afe5c4f74bbf6e66340f1"
            )
            return response.json()
        except requests.RequestException as e:
            print(f"Error fetching weather data: {e}")
            return {"error": "Failed to fetch weather data"}

    @method_decorator(cache_page(60 * 20))
    def get(self, request, *args, **kwargs):
        weather_detail = self.get_weather_information_open_weather()
        return Response(data=weather_detail)

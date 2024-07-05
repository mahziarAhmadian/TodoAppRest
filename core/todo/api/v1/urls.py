from django.urls import path, include
from .views import TaskModelViewSet
from .views import WeatherGenericAPIView
app_name = "api-v1"

urlpatterns = [
    path('task/', TaskModelViewSet.as_view({
        'get': 'list',
        'post': 'create',
    }), name="task-list"),

    path('task/<int:pk>/', TaskModelViewSet.as_view({
        'put': 'update',
        'patch': 'partial_update',
        'get': 'retrieve',
        'delete': 'destroy',
    }),
         name="task-detail"),

    path('weather/information/', WeatherGenericAPIView.as_view(), name="weather-detail"),
]

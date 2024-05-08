from django.urls import path, include
from .views import TaskModelViewSet

urlpatterns = [
    path('task/', TaskModelViewSet.as_view({
        'get': 'list',
        'post': 'create',
    }), name="task list"),

    path('task/<int:pk>/', TaskModelViewSet.as_view({
        'put': 'update',
        'patch': 'partial_update',
        'get': 'retrieve',
        'delete': 'destroy',
    }),
         name="detail"),
]

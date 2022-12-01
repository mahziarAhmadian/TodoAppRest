from django.urls import path, include
from .views import TaskModelViewSet

GetAllTask = TaskModelViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
GetOne = TaskModelViewSet.as_view(
    {
        'put': 'update',
        'patch': 'partial_update',
        'get': 'retrieve',
        'delete': 'destroy',
    }
)
urlpatterns = [

    path('get/', GetAllTask, name="task list"),
    path('get/<int:pk>/', GetOne, name="task get one "),

]

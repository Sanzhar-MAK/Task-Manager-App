from django.urls import path
from . api_views import TaskListCreateApiView
from . import api_views

urlpatterns = [
    # path('api/tasks/', api_views.task_api_list, name='task_api_list'),
    # path('api/tasks/<int:pk>', api_views.task_api_detail, name='task_api_detail'),
    path('api/tasks/', TaskListCreateApiView.as_view(), name='task_api_list'),
    path('api/tasks/<int:pk>', TaskListCreateApiView.as_view(), name='task_api_detail'),
]
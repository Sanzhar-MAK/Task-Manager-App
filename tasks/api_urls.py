from django.urls import path
from . api_views import TaskListCreateApiView, TaskDetailApiView, TaskViewSet
from . import api_views
from rest_framework import routers

# urlpatterns = [
#     # path('api/tasks/', api_views.task_api_list, name='task_api_list'),
#     # path('api/tasks/<int:pk>', api_views.task_api_detail, name='task_api_detail'),
#     path('tasks/', TaskListCreateApiView.as_view(), name='task_api_list'),
#     path('tasks/<int:pk>/', TaskDetailApiView.as_view(), name='task_api_detail'),
# ]

router = routers.SimpleRouter()
router.register(r'tasks', TaskViewSet, basename='task')
urlpatterns = router.urls

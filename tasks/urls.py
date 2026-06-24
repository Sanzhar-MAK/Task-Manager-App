from django.urls import path
from . import views

urlpatterns = [
    path('', views.task_list, name='task_list'),
    path('task/<int:pk>/', views.task_detail, name='task_detail'),
    path('task/new/', views.task_new, name='task_new'),
    path('task/<int:pk>/edit', views.task_edit, name='task_edit')
]
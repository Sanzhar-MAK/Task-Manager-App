from django.urls import path
from . import views

urlpatterns = [
    path('', views.user_login, name='user_login'),
    path('register', views.user_register, name='user_register'),
    path('logout', views.user_logout, name='user_logout'),
    path('tasks', views.task_list, name='task_list'),
    path('profile', views.user_profile, name='user_profile'),
    path('task/<int:pk>/', views.task_detail, name='task_detail'),
    path('task/new/', views.task_new, name='task_new'),
    path('task/<int:pk>/edit/', views.task_edit, name='task_edit'),
    path('task/<int:pk>/remove/', views.task_remove, name='task_remove'),

    path('api/tasks/', views.task_api_list, name='task_api_list')
]
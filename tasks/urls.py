from django.urls import path
from . import views

urlpatterns = [
    path('', views.app_list, name='app_list')
]
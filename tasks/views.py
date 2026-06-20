from django.shortcuts import render
from .models import Task
from django.utils import timezone

# Create your views here.

def app_list(request):
    tasks = Task.objects.filter(created_at__lte=timezone.now()).order_by('created_at')
    return render(request, 'tasks/app_list.html', {'tasks': tasks})

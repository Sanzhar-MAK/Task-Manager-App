from django.shortcuts import render, get_object_or_404
from .models import Task
from django.utils import timezone

# Create your views here.

def task_list(request):
    tasks = Task.objects.filter(created_at__lte=timezone.now()).order_by('created_at')
    return render(request, 'tasks/task_list.html', {'tasks': tasks})

def task_detail(request, pk):
    task = get_object_or_404(Task, pk=pk)
    return render(request, 'tasks/task_detail.html', {'task': task})
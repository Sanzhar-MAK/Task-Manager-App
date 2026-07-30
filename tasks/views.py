from django.shortcuts import render, get_object_or_404, redirect
from .models import Task
from .forms import TaskForm, UserRegisterForm, UserLoginForm
from django.utils import timezone
from django.contrib.auth import authenticate, login, logout
from django.contrib.messages import constants as messages
from django.contrib.auth.decorators import login_required

@login_required
def task_list(request):
    tasks = Task.objects.filter(created_at__lte=timezone.now()).order_by('created_at')
    return render(request, 'tasks/task_list.html', {'tasks': tasks})

@login_required
def task_detail(request, pk):
    task = get_object_or_404(Task, pk=pk)
    return render(request, 'tasks/task_detail.html', {'task': task})

@login_required
def task_new(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.author = request.user
            task.created_at = timezone.now()
            task.save()
            return redirect('task_detail', pk=task.pk)
    else:
        form = TaskForm()
    return render(request, 'tasks/task_edit.html', {'form':form})

@login_required   
def task_edit(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            task = form.save(commit=False)
            task.author = request.user
            task.created_at = timezone.now()
            task.save()
            return redirect('task_detail', pk=task.pk)
    else:
        form = TaskForm(instance=task)
    return render(request, 'tasks/task_edit.html', {'form':form})

@login_required
def task_remove(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        task.delete()
    return redirect('task_list')
    

def user_login(request):
    if request.method == 'POST':
        login_form = UserLoginForm(request, data=request.POST)
        if login_form.is_valid():
            login(request, login_form.get_user())
            return redirect('task_list')
    else:
        login_form = UserLoginForm() 
    return render(request, 'registration/user_login.html',{'login_form': login_form})

def user_logout(request):
    logout(request)
    return redirect('user_login')

def user_register(request):
    if request.method == 'POST':
        reg_form = UserRegisterForm(request.POST)
        if reg_form.is_valid():
            reg_form.save()
            return redirect('user_login')
    else:
        reg_form = UserRegisterForm()
    return render(request, 'registration/user_register.html',{'reg_form':reg_form})
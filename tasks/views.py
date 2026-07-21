from django.shortcuts import render, get_object_or_404, redirect
from .models import Task
from .forms import TaskForm, UserRegisterForm, UserLoginForm
from django.utils import timezone


def task_list(request):
    tasks = Task.objects.filter(created_at__lte=timezone.now()).order_by('created_at')
    return render(request, 'tasks/task_list.html', {'tasks': tasks})

def task_detail(request, pk):
    task = get_object_or_404(Task, pk=pk)
    return render(request, 'tasks/task_detail.html', {'task': task})

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

def task_remove(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        task.delete()
    return redirect('task_list')
    

def user_login(request):
    login_form = UserLoginForm()
    if request.method == 'POST':
        if login_form.is_valid():
            print('form is valid')
        else:
            print('form is not valid')
    return render(request, 'registration/user_login.html',{'login_form': login_form})

def user_register(request):
    if request.method == 'POST':
        reg_form = UserRegisterForm(request.POST)
        if reg_form.is_valid():
            reg_form.save()
            return redirect('user_login')
    else:
        reg_form = UserRegisterForm()
    return render(request, 'registration/user_register.html',{'reg_form':reg_form})
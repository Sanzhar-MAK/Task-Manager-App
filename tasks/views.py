from django.shortcuts import render

# Create your views here.

def app_list(request):
    return render(request, 'tasks/app_list.html', {})
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status, generics, viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.filters import SearchFilter

from .models import Task
from .serializers import TaskSerializer

class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    def get_queryset(self):
        return Task.objects.filter(author=self.request.user)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    filter_backends = [SearchFilter]
    search_fields = ["title"]

class TaskListCreateApiView(generics.ListCreateAPIView):
    serializer_class = TaskSerializer

    def get_queryset(self):
        return Task.objects.filter(author=self.request.user)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class TaskDetailApiView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TaskSerializer

    def get_queryset(self):
        return Task.objects.filter(author=self.request.user)

@api_view(["GET", "POST"])
@permission_classes([IsAuthenticated])
def task_api_list(request):
    if request.method == "GET":
        tasks = Task.objects.filter(author=request.user)
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)

    if request.method == "POST":
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(author=request.user)
            return Response(serializer.data)
        return Response(serializer.errors)

@api_view(["GET", "DELETE", "PATCH", "PUT"])
@permission_classes([IsAuthenticated])
def task_api_detail(request, pk): 
    if request.method == "GET":
        task = get_object_or_404(
            Task,
            pk=pk,
            author=request.user
        )
        serializer = TaskSerializer(task)    
        return Response(serializer.data)
    
    if request.method == "DELETE":
        task = get_object_or_404(
            Task,
            pk=pk,
            author=request.user
        )
        task.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)

    if request.method == "PATCH":
        task = get_object_or_404(
            Task,
            pk=pk,
            author=request.user
        )
        serializer = TaskSerializer(instance=task, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    if request.method == "PUT":
        task = get_object_or_404(
            Task,
            pk=pk,
            author=request.user
        )
        serializer = TaskSerializer(instance=task, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
@api_view(["GET", "DELETE"])
@permission_classes([IsAuthenticated])
def task_api_delete(request, pk):
    task = get_object_or_404(Task, pk=pk, author = request.user)
    if request.method == "POST":
        serializer = TaskSerializer(task)
        serializer.delete()
    return Response(serializer.data)
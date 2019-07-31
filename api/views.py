from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from .serializers import TaskSerializer, TaskMiniSerializer
from .models import Task
from rest_framework.response import Response


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    
    def list(self, request, *args, **kwargs):
        tasks = Task.objects.all()
        serializer = TaskMiniSerializer(tasks, many=True)
        return Response(serializer.data)

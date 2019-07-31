from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Task


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'title', 'desc', 'done']


class TaskMiniSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'title']

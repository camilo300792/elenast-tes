
# DRF imports
from functools import partial
import imp
from os import stat
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

# Eleneas import
from .models import Task
from .serializers import TaskSerializer
from .permissions import IsOwnerOrReadOnly

"""Create Task view"""
class TaskListView(generics.ListCreateAPIView):
    # queryset = Task.objects.all()
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = TaskSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_queryset(self):

        queryset = Task.objects.all()
        queryset = Task.objects.filter(owner_id=self.request.user.id)
        title = self.request.query_params.get('title')
        description = self.request.query_params.get('description')
        status = self.request.query_params.get('status')

        if title is not None:
            queryset = queryset.filter(title=title)
        if description is not None:
            queryset = queryset.filter(description=description)
        if status is not None:
            queryset = queryset.filter(status=status)

        return queryset

"""Retrieve update or delete, task"""
class TaskDetailAPIView(generics.RetrieveUpdateDestroyAPIView):

    queryset = Task.objects.all()
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]
    serializer_class = TaskSerializer
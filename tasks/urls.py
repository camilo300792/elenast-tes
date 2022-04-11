# Django imports
from django.urls import path
# elenas import
from .views import TaskDetailAPIView, TaskListView

urlpatterns = [
    path('tasks/', TaskListView.as_view(), name='tasks'),
    path('tasks/<int:pk>', TaskDetailAPIView.as_view(), name='tasks_detail'),
]
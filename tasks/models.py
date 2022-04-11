# django imports
from django.db import models
from django.utils.translation import gettext_lazy as __
from django.contrib.auth.models import User

# Create your models here.

class Task(models.Model):

    class TaskStatus(models.TextChoices):

        PENDING = 'P', __('Pending')
        IN_REVIEW = 'IR', __('In Review')
        IN_PROCESS = 'IP', __('In Process')
        COMPLETED = 'C', __('Completed')

    title = models.CharField(
        verbose_name='task title', 
        max_length=75
    )

    description = models.TextField(
        verbose_name='Task description',
        max_length=255
    )

    status = models.CharField(
        max_length=2,
        choices=TaskStatus.choices,
        default=TaskStatus.PENDING
    )

    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f'{self.title}={self.status}'
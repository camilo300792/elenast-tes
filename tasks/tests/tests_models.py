from asyncio import tasks
from django.test import TestCase
from tasks.models import Task
# Create your tests here.

class TaskModelTestCase(TestCase):

    def setUp(self) -> None:
        Task.objects.create(title="ToDo", description="ToDo list")

    def test_task_name_is_title_and_status(self) -> None:
        task = Task.objects.get(pk=1)
        expected_object_name = f'{task.title}={task.status}'
        self.assertEquals(expected_object_name, str(task))

    def test_task_status_is_pending_after_create(self) -> None:
        task = Task.objects.get(title="ToDo")
        expected_status = 'P'
        self.assertEquals(expected_status, task.status)
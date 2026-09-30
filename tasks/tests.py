from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from tasks.models import Task

class TaskApiTest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="sanzhar",
            password="test"
        )
        self.task = Task.objects.create(
            title = "Test title"
            author=self.user
        )


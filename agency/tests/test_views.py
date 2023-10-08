from django.contrib.auth import get_user_model
from django.test import TestCase

from agency.models import Topic, Newspaper


class PublicTests(TestCase):
    def setUp(self):
        topic1 = Topic.objects.create(name="Test1")
        topic2 = Topic.objects.create(name="Test2")

        redactor1 = get_user_model().objects.create_user(
            username="Test_user1", password="test1234"
        )
        redactor2 = get_user_model().objects.create_user(
            username="Test_user2", password="test1234"
        )

        newspaper1 = Newspaper.objects.create(
            title="Test1", content="empty", topic=topic1
        )
        newspaper2 = Newspaper.objects.create(
            title="Test2", content="empty", topic=topic2
        )

        newspaper1.publishers.add(redactor1)
        newspaper2.publishers.add(redactor2)

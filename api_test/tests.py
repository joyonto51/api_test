from rest_framework.test import APITestCase, APIClient
from django.urls import reverse
from rest_framework.views import status

from api_test.serializers import BookSerializer
from .models import Book

# Create your tests here.

class BaseViewTest(APITestCase):
    @staticmethod
    def create_book(name=''):
        if name != '':
            Book.objects.create(name="Python")

    def setUp(self):
        # add test data
        self.create_book("The Angels",)
        self.create_book("Dataset",)
        self.create_book("C Programming",)
        self.create_book("Python3",)


class GetAllSongsTest(BaseViewTest):
    def test_books(self):
        response = self.client.get(
            reverse("all_books", kwargs={'id':1})
        )

        expected = Book.objects.all()
        serialized = BookSerializer(expected, many=True)
        self.assertEqual(response.data, serialized.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
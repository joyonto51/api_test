from rest_framework import serializers

from api_test.models import Book


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('name','writter', 'author')
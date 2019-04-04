from tastypie.resources import ModelResource
from api_test.models import Book
from tastypie.authorization import DjangoAuthorization

class BookResource(ModelResource):
    class Meta:
        queryset = Book.objects.all()
        resource_name = 'book'
        authorization = DjangoAuthorization()
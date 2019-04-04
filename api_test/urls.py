from django.urls import path
from .views import BookListView

urlpatterns=[
    path('books/<int:id>/', BookListView.as_view(), name='all_books')
]
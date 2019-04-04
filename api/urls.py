from django.urls import path, include
from .views import ListTodo, DetailTodo, login, sample_api

urlpatterns = [
    path('', ListTodo.as_view(), name='todo_list'),
    path('<int:pk>/', DetailTodo.as_view(), name='todo_details'),
    path('rest-auth/', include('rest_auth.urls')),
    path('login/', login),
    path('sample-api/', sample_api),
]
from django.urls import path
from .views import ExampleView, CustomAuthToken


urlpatterns = [
    path('login/', ExampleView.as_view(), name='example'),
]
urlpatterns += [
    path('api-token-auth/', CustomAuthToken.as_view())
]
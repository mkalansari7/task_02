from django.urls import path
from restaurants import views

urlpatterns = [
    path("hello/", views.hello, name='hello-world')
]
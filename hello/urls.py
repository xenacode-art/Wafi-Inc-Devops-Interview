# healthcheck/urls.py
from django.urls import path
from .views import health_check, hello_devops

urlpatterns = [
    path("health/", health_check, name="health_check"),
    path("hello/", hello_devops, name="hello_devops"),
]

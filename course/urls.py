from django.urls import path
from .views import *


app_name = "course"

urlpatterns = [
    path("", course, name="courses"),
    path("trainer", trainer, name="trainers"),
]
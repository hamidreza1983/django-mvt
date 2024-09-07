from django.urls import path
from .views import (
    home, contact, about, events
)

app_name = "root"

urlpatterns = [
    path("", home, name="home"),
    path("contactus", contact, name="contact"),
    path("aboutus", about, name="about"),
    path("events", events, name="events"),
]
from django.db import models
from django.utils import timezone


class Serivces(models.Model):
    name = models.CharField(max_length=100)
    content = models.TextField(default="test")  
    status = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ('created_at',)

class Events(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="events", default="events_2.jpg")
    scheduled = models.DateTimeField(default=timezone.now)
    content = models.TextField(default="test")  
    status = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ('created_at',)

class NewsLetter(models.Model):
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.email
    

class ContactUs(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    subject = models.CharField(max_length=200)
    message = models.TextField()

    def __str__(self):
        return self.email
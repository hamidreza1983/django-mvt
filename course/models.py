from django.db import models
#from django.contrib.auth.models import User
from django.utils import timezone
from django.contrib.auth import get_user_model
User = get_user_model()



class Category(models.Model):
    name = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["created_at"]

    def __str__(self):
        return self.name
    
class Skills(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["created_at"]
    def __str__(self):
        return self.name

class Trainer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="trainer", default="default.jpg")
    skills = models.ManyToManyField(Skills)
    description = models.TextField()
    twitter = models.CharField(max_length=120)
    facebook = models.CharField(max_length=120)
    instagram = models.CharField(max_length=120)
    linkedin = models.CharField(max_length=120)
    status = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["created_at"]

    def __str__(self):
        return self.user.username

class Courses(models.Model):
    name = models.CharField(max_length=120)
    fee = models.FloatField(default=10.5)
    capacity = models.IntegerField(default=10)
    schedule = models.DateTimeField(default=timezone.now)
    image = models.ImageField(upload_to="course", default="images.png")
    trainer = models.ForeignKey(Trainer, on_delete=models.CASCADE)
    content = models.TextField()
    category = models.ManyToManyField(Category)
    status = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ["created_at"]

    def __str__(self):
        return self.name
    
class Comments(models.Model):
    course = models.ForeignKey(Courses, on_delete=models.CASCADE)
    name = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    status = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name.username
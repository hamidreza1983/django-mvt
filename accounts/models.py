from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone



class CustomUserModel(AbstractUser):
    image = models.ImageField(upload_to="user", default="user-image.png")
    id_code = models.CharField(max_length=10, unique=True)
    mobile = models.CharField(max_length=11, unique=True)
    address = models.CharField(max_length=220)
    birthday = models.DateTimeField(default=timezone.now)



class PersonalToken(models.Model):
    user = models.ForeignKey(CustomUserModel, on_delete=models.CASCADE)
    token = models.CharField(max_length=255)

    def __str__(self):
        return self.user.email


# Create your models here.

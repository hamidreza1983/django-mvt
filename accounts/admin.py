from django.contrib import admin
from .models import PersonalToken
from .models import CustomUserModel

admin.site.register(PersonalToken)
admin.site.register(CustomUserModel)

# Register your models here.

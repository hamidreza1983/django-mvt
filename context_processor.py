from root.models import Events
from course.models import *
from django.contrib.auth import get_user_model
User = get_user_model()




def general_objects(request):
    context = {
        "events_count": Events.objects.all().count(),
        "users_count" : User.objects.all().count(),
        "courses_count" : Courses.objects.all().count(),
        "category" : Category.objects.all(),
        "trainers_count" : Trainer.objects.all().count(),
    }

    return context
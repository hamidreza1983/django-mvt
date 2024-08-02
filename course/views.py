from django.shortcuts import render
from .models import Courses, Trainer

# Create your views here.


def course(request):
    courses = Courses.objects.filter(status=True)
    context = {
        "courses" : courses
    }
    return render(request, 'course/courses.html', context=context)


def trainer(request):
    trainers = Trainer.objects.filter(status=True)
    context = {
        "trainers" : trainers
    }
    return render(request, 'course/trainers.html', context=context)

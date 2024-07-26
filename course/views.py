from django.shortcuts import render
from .models import Courses

# Create your views here.


def course(request):
    courses = Courses.objects.filter(status=True)
    context = {
        "courses" : courses
    }
    return render(request, 'course/courses.html', context=context)
from django.shortcuts import render, get_object_or_404
from .models import Courses, Trainer

# Create your views here.


def course(request, **kwargs):
    if request.GET.get('search') is not None:
        courses = Courses.objects.filter(content__contains=request.GET.get('search'))
    elif kwargs.get('tr') is not None:
        courses = Courses.objects.filter(trainer__user__username=kwargs.get('tr'))
    elif kwargs.get('catname') is not None:
        courses = Courses.objects.filter(category__name=kwargs.get('catname')) 
    elif kwargs.get('pr') is not None:
        courses = Courses.objects.filter(fee__lte=float(kwargs.get('pr')))
    else:
        courses = Courses.objects.filter(status=True)
    context = {
        "courses" : courses
    }
    return render(request, 'course/courses.html', context=context)


def course_detail(request, id):
    course = get_object_or_404(Courses, id=id)
    context = {
        "course" : course
    }
    return render(request, 'course/course-details.html', context=context)


def trainer(request):
    trainers = Trainer.objects.filter(status=True)
    context = {
        "trainers" : trainers
    }
    return render(request, 'course/trainers.html', context=context)

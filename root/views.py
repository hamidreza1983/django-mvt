from django.shortcuts import render
from .models import Serivces, Events
from course.models import Courses, Trainer




def home(request):
    #services = Serivces.objects.all()
    print (request.GET)
    last_three_courses = Courses.objects.filter(status=True)[:3]
    last_three_trainers = Trainer.objects.filter(status=True)[:3]
    services = Serivces.objects.filter(status=True)
    context={
        "services": services,
        "ltc":last_three_courses,
        "ltt":last_three_trainers,
    }
    return render(request, 'root/index.html', context = context )

def contact(request):
    return render(request, 'root/contact.html')

def about(request):
    return render(request, 'root/about.html')

def events(request):
    event = Events.objects.all()
    context = {
        "events": event
    }
    return render(request, 'root/events.html', context = context)

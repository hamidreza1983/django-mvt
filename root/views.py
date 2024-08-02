from django.shortcuts import render
from .models import Serivces, Events



def home(request):
    #services = Serivces.objects.all()
    services = Serivces.objects.filter(status=True)
    return render(request, 'root/index.html', context={"services": services})

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

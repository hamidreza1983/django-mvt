from django.shortcuts import render, redirect
from .models import Serivces, Events
from course.models import Courses, Trainer
from .forms import NewsLetterForm, ContactUsForm
from django.contrib import messages




def home(request):
    last_three_courses = Courses.objects.filter(status=True)[:3]
    last_three_trainers = Trainer.objects.filter(status=True)[:3]
    services = Serivces.objects.filter(status=True)
    if request.method == "GET":
        form = NewsLetterForm()
        context={
            "services": services,
            "ltc":last_three_courses,
            "ltt":last_three_trainers,
            "form":form
        }
        return render(request, 'root/index.html', context = context )
    elif request.method == "POST":
        form = NewsLetterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("root:home")
        else:
            messages.add_message(request, messages.ERROR , "please insert another email")
            return redirect(request.path_info)



def contact(request):
    if request.method == "GET":
        return render(request, 'root/contact.html')
    elif request.method == "POST":
        form = ContactUsForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, "we receive your data and call with you as soon")
            return redirect("root:contact")
        else:
            messages.add_message(request, messages.ERROR, "please insert correct data")
            return redirect("root:contact")


def about(request):
    return render(request, 'root/about.html')

def events(request):
    event = Events.objects.all()
    context = {
        "events": event
    }
    return render(request, 'root/events.html', context = context)

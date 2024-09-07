from django.shortcuts import render, get_object_or_404, redirect
from .models import Courses, Trainer, Comments
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from .forms import CommentForm
from django.contrib import messages

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

    courses = Paginator(courses, 4)

    try:
        page_number = request.GET.get('page')
        courses = courses.get_page(page_number)
    except EmptyPage:
        courses = courses.get_page(1)
    except PageNotAnInteger:
        courses = courses.get_page(1)

    context = {
        "courses" : courses,
         "page_number" : page_number
    }
    return render(request, 'course/courses.html', context=context)


def course_detail(request, id):
    if request.method == "GET":
        course = get_object_or_404(Courses, id=id)
        comments = Comments.objects.filter(status=True, course=course)
        context = {
            "course" : course,
            "comments" : comments,
        
        }
        return render(request, 'course/course-details.html', context=context)
    elif request.method == "POST":
        if request.user.is_authenticated:
            form = CommentForm(request.POST)
            if form.is_valid():
                form.save()
                messages.add_message(request, messages.SUCCESS, "valid data")
                return redirect (request.path_info)
            else:
                messages.add_message(request, messages.ERROR, "Invalid data")
                return redirect (request.path_info)
        else:
            return redirect ("accounts:login")

def trainer(request):
    trainers = Trainer.objects.filter(status=True)
    context = {
        "trainers" : trainers
    }
    return render(request, 'course/trainers.html', context=context)


def edit_comment(request, id):
    comment = get_object_or_404(Comments, id=id)
    if request.method == "GET":
       
        form = CommentForm(instance=comment)
        context = {
            "form" : form,
        }
        return render(request, 'course/edit.html', context=context)
    
    elif request.method == "POST":
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.status = False
            comment.save()
            return redirect("course:courses")


from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .forms import LoginForm
from django.contrib.auth import authenticate, login, logout, password_validation
from django.contrib import messages
from django.contrib.auth.decorators import login_required



def login_view(request):
    if request.method == 'GET':
        form = LoginForm()
        context = {
            'form' : form,
        }
        return render(request, 'registration/login.html', context=context)
    elif request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("/")
            else:
                messages.add_message(request, messages.ERROR, "Login failed please check you input data and try again ")
                return redirect(request.path_info)
        else:
            messages.add_message(request, messages.ERROR, "Login failed please check you input data and try again ")
            return redirect(request.path_info)
        
@login_required()
def logout_view(request):
    logout(request)
    return redirect("/")





# Create your views here.

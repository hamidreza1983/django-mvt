from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .forms import LoginForm
from django.contrib.auth import authenticate, login, logout, password_validation
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import RegistrationForm, ChangePassword



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

def signup(request):
    if request.method == "GET":
        form = RegistrationForm()
        context = {
            "form" : form,
        }
        return render(request,"registration/signup.html", context=context)
    else:
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login (request, user)
            return redirect("/")
        else:
            messages.add_message(request, messages.ERROR, "input data is not valid ")
            return redirect(request.path_info)

@login_required()
def password_change(request):
    if request.method == "GET":
        form = ChangePassword()
        context = {
            "form" : form
        }
        return render (request,"registration/change_pass.html", context=context)
    else:
        user = request.user
        current_password = request.POST.get('current_password')
        if not user.check_password(current_password):
            messages.add_message(request, messages.ERROR, "old password is not same")
            return redirect(request.path_info)
        pass1 = request.POST.get('password')
        pass2 = request.POST.get('confirm_password')
        if pass1 != pass2 :
            messages.add_message(request, messages.ERROR, "pass1 and pass2 must be the same")
            return redirect(request.path_info)
        try : 
            password_validation.validate_password(pass1)
            user.set_password(pass1)
            user.save()
            messages.add_message(request, messages.SUCCESS, "password change succesfully")
            return redirect(request.path_info)
        except:
            messages.add_message(request, messages.ERROR, "password validation fail")
            return redirect(request.path_info)



        



def password_reset(request):
    pass

def password_reset_done(request):
    pass


def password_reset_confirm(request):
    pass

def password_reset_complete(request):
    pass



# Create your views here.

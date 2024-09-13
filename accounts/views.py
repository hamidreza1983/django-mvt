from django.shortcuts import render, redirect, get_object_or_404
#from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from .forms import (
    LoginForm, RegistrationForm, PasswordResetConfirmForm,
    ChangePassword, EditProfileForm, PasswordResetForm, 
)
from django.contrib.auth import authenticate, login, logout, password_validation
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from uuid import uuid4
from .models import PersonalToken
from threading import Thread


User = get_user_model()

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
            username_or_email = form.cleaned_data['username_or_email']
            password = form.cleaned_data['password']
            if "@" in username_or_email:
                username = User.objects.get(email=username_or_email).username
                user = authenticate(username=username, password=password)
                if user is not None:
                    login(request, user)
                    return redirect("/")
                else:
                    messages.add_message(request, messages.ERROR, "Login failed please check you input data and try again ")
                    return redirect(request.path_info)
            else:
                user = authenticate(username=username_or_email, password=password)
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
    if request.method == "GET":
        form = PasswordResetForm()
        context = {
            "form" : form
        }
        return render(request, "registration/reset_password.html", context=context)
    else:
        form = PasswordResetForm(request.POST)
        if form.is_valid():
            user = get_object_or_404(User, email=form.cleaned_data["email"])
            try:
                token = PersonalToken.objects.get(user=user)
            except:
                token = PersonalToken.objects.create(user=user, token=str(uuid4()))
            subject = "reset password",
            message = f"http://127.0.0.1:8000/accounts/password_reset_confirm/{token.token}",
            #message = f"http://learningpy.ir/accounts/password_reset_confirm/{token.token}",
            sender = "admin",
            receiver = [user.email],
            fail_silently=True
            send_mail(
                subject=subject,
                message=message,
                from_email=sender,
                recipient_list=receiver,
                fail_silently=True
            )
            return redirect("accounts:password_reset_done")
        else:
            messages.add_message(request, messages.ERROR, "please inser correct data")
            return redirect(request.path_info)
        
def password_reset_done(request):
    return render(request, "registration/password_reset_done.html")

def password_reset_confirm(request, token):
    if request.method == "GET":
        form = PasswordResetConfirmForm()
        context = {
            "form" : form,
        }
        return render (request, "registration/password_reset_confirm.html", context=context)
    else:
        user = PersonalToken.objects.get(token=token).user
        pass1 = request.POST.get('pass1')
        pass2 = request.POST.get('pass2')
        if pass1 != pass2 :
            messages.add_message(request, messages.ERROR, "pass1 and pass2 must be the same")
            return redirect(request.path_info)
        try : 
            password_validation.validate_password(pass1)
            user.set_password(pass1)
            user.save()
            return redirect("accounts:password_reset_complete")
        except:
            messages.add_message(request, messages.ERROR, "password validation fail")
            return redirect(request.path_info)

def password_reset_complete(request):
    return render (request, "registration/password_reset_complete.html")

def edit_profile(request, id):
    user = User.objects.get(id=id)
    if request.method == "GET":
        form = EditProfileForm(instance=user)
        context = {
            "form" : form
        }
        return render (request,"registration/edit-profile.html", context=context)
    else:
        form = EditProfileForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return redirect("/")
        else:
            messages.add_message(request, messages.ERROR, "invalid data input")
            return redirect(request.path_info)

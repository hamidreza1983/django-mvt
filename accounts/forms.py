#from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django import forms
from django.contrib.auth.forms import UserCreationForm
from captcha.fields import CaptchaField

User = get_user_model()

class LoginForm(forms.Form):
    username_or_email = forms.CharField(max_length=100)
    password = forms.CharField(max_length=20, widget=forms.PasswordInput)
    captcha = CaptchaField()

class RegistrationForm(UserCreationForm):

    class Meta:
        model = User
        fields = ["id_code", "email", "mobile", "username", "password1", "password2"]


class ChangePassword(forms.Form):
    current_password = forms.CharField(max_length=100, widget=forms.PasswordInput)
    password = forms.CharField(max_length=20, widget=forms.PasswordInput)
    confirm_password = forms.CharField(max_length=20, widget=forms.PasswordInput)

class PasswordResetForm(forms.Form):
    email = forms.EmailField()

class PasswordResetConfirmForm(forms.Form):
    pass1 = forms.CharField(max_length=20, widget=forms.PasswordInput)
    pass2 = forms.CharField(max_length=20, widget=forms.PasswordInput)



class EditProfileForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ["first_name", "last_name", "birthday", "address", "image"]
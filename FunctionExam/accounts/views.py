from django.shortcuts import render, redirect
from . import forms
from django.core.exceptions import ValidationError
from .models import UserActivateTokens
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    return render(
        request, "accounts/home.html"
    )

def regist(request):
    regist_form = forms.RegistForm(request.POST or None)
    if regist_form.is_valid():
        try:
            regist_form.save()
            return redirect("accounts:home")
        except ValidationError as err:
            regist_form.add_error("password", err)

    return render(
        request, 'accounts/register.html', context={
            'regist_form': regist_form
        }
    )

def activate_user(request, token):
    user_activate_token = UserActivateTokens.objects.activate_user_by_token(token)
    return render(request, "accounts/activate_user.html")

def user_login(request):
    login_form = forms.LoginForm(request.POST or None)
    if login_form.is_valid():
        email = login_form.cleaned_data.get("email")
        password = login_form.cleaned_data.get("password")
        user = authenticate(email=email, password=password)
        if user:
            if user.is_active:
                login(request, user)
                messages.success(request, "Login successfully")
                return redirect("accounts:home")
            else:
                messages.warning(request, "User unknown.")
        else:
            messages.warning(request, "User or password is wrong.")
    return render(
        request, "accounts/user_login.html", context={
            "login_form": login_form,
        }
    )

@login_required
def user_logout(request):
    logout(request)
    messages.success(request, "Logged out.")
    return redirect("accounts:home")

@login_required
def user_edit(request):
    user_edit_form = forms.UserEditForm(request.POST or None, request.FILES or None, instance=request.user)
    if user_edit_form.is_valid():
        user_edit_form.save()
        return render(request, "accounts/user_edit.html", context={
            "user_edit_form": user_edit_form
        })
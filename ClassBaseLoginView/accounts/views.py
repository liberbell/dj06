from django.shortcuts import render
from django.views.generic.edit import CreateView, FormView
from django.views.generic.base import TemplateView, View
from .forms import RegistForm

# Create your views here.
class HomeView(TemplateView):
    template_name = "home.html"

class RegistUserView(CreateView):
    template_name = "regist.html"
    form_class = RegistForm

class UserLoginView(FormView):
    template_name = "user_login.html"
    form_class = UserLoginForm

class UserLogoutView(View):
    pass

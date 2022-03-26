from django.shortcuts import render
from user.forms import UserForm, ProfileForm

# Create your views here.
def user_list(request):
    return render(request, "user/user_list.html")

def index(request):
    return render(request, "user/index.html")

def register(request):
    user_form = UserForm(request.POST or None)
    profile_home = ProfileForm(request.POST or None, request.FILES or None)
    if user_form.is_valid() and profile_home.is_valid():
        user = user_form.save()
        user.set_password(user.password)
        user.save()
        profile = profile_home.save(commit=False)
        profile.user = user
        profile.save()

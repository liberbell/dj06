from django.shortcuts import render

# Create your views here.
def user_list(request):
    return render(request, "user/user_list.html")

def index(request):
    return render(request, "user/index.html")
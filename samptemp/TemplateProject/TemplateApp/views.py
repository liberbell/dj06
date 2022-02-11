from django.shortcuts import render

# Create your views here.
def index(request):
    val = "This is the value input."
    return render(request, 'TemplateApp/index.html', context={'value': val})

def home(request):
    my_name = "Eric Crapton"
    favorite_fruit = ["Apple", "Grape", "Lemon"]
    my_info = {
        "name": "Eric",
        "age": 70
    }

    return render(request, "home.html", context={
        "my_name": my_name,
        "favorite_fruit": favorite_fruit,
        "my_info": my_info
    })
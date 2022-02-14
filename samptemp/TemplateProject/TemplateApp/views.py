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
    status = 20

    return render(request, "home.html", context={
        "my_name": my_name,
        "favorite_fruit": favorite_fruit,
        "my_info": my_info
    })

def sample1(request):
    return render(request, "sample1.html")

def sample2(request):
    return render(request, "sample2.html")

def sample(request):
    name = "Alex Hep"
    height = 172.4
    weight = 56
    bmi = weight / (height / 100) ** 2
    page_url = "HomePage: https://www.google.com"
    favorite_fruit = [
        "Apple",
        "Strawberry",
        "Peach"
    ]
    message1 = '''Hello
    My name is
    Alex.
    '''
    message2 = "1234567890"
    salary = 34000
    status = 20
    return render(request, "sample.html", context={
        "name": name,
        "height": height,
        "weight": weight,
        "bmi": bmi,
        "page_url": page_url,
        "favorite_fruit": favorite_fruit,
        "message1": message1,
        "message2": message2,
        "salary": salary,
        "status": status
    })
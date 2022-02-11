from django.shortcuts import render

# Create your views here.
def index(request):
    val = "This is the value input."
    return render(request, 'TemplateApp/index.html', context={'value': val})
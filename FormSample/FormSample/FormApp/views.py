from django.shortcuts import render
from . import forms

# Create your views here.
def index(request):
    return render(request, "formapp/index.html")

def form_page(request):
    form = forms.UserInfo()
    if request.method == "POST":
        form = forms.UserInfo(request.POST)
        if form.is_valid:
            print("Validation Success")
            print(f'name: {form.cleaned_data["name"]}, mail: {form.cleaned_data["mail"]}')
    return render(
        request,
        "formapp/form_page.html",
        context={"form": form }
    )
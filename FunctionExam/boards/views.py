from django.shortcuts import render, redirect, get_object_or_404
from . import forms
from django.contrib import messages
from .models import Themes
from django.http import Http404

# Create your views here.
def create_theme(request):
    create_theme_form = forms.CreateThemeForm(request.POST or None)
    if create_theme_form.is_valid():
        create_theme_form.instance.user = request.user
        create_theme_form.save()
        messages.success(request, "Create Board successfully.")

        return redirect("boards:list_themes")
    return render(request, "boards/create_theme.html", context={
        "create_theme_form": create_theme_form
    })

def list_themes(request):
    themes = Themes.objects.fetch_all_themes()
    return render(request, "boards/list_themes.html", context={
        "themes": themes
    })

def edit_theme(request, id):
    theme = get_object_or_404(Themes, id=id)
    if theme.user.id != request.user.id:
        raise Http404
    edit_theme_form = forms.CreateThemeForm(request.POST or None, instance=theme)
    if edit_theme_form.is_valid():
        edit_theme_form.save()
        messages.success(request, "Update theme")
        return redirect("boards:list_themes")
    return render(request, "boards/edit_theme.html", context={
        "edit_theme_form": edit_theme_form,
        "id": id,
    })
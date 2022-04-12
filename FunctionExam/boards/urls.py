from unicodedata import name
from django.urls import path
from . import views

app_name = "boards"

urlpatterns = [
    path("create_theme", views.create_theme, name="create_theme"),
    path("list_theme", views.list_theme, name="list_theme"),
]

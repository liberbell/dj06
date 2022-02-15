from urllib.parse import urlparse
from django.urls import path
from . import views

app_name = "app"

urlpatterns = [
    path("", views.home, name="home"),
    path("members", views.members, name="members"),
    path("member/<int:id>", views.members, name="members")
]

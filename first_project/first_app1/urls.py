from unicodedata import name
from django.urls import path
from . import views

app_name = 'first_app1'

urlpatterns = [
    path('hello', views.index, name='index'),
]

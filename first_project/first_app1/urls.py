from unicodedata import name
from django.urls import path
from . import views

app_name = 'first_app1'

urlpatterns = [
    path('hello', views.index, name='index'),
    path('page/<str:user_name', views.user_page, name='user_page')
]

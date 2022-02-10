from django.urls import path
from . import views

app_name = 'first'

urlpatterns = [
    path('add/<int:num1>/<int:num2>', views.add, name='add'),
]

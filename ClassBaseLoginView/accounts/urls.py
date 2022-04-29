from django.urls import path
from .views import (
    RegistUserView, UserLoginView, HomeView, UserLogoutView
)

app_name = "accounts"

urlpatterns = [
    path("home/", HomeView.as_view, name="home"),
    path("regist/", RegistUserView.as_view, name="regist"),
    path("user_login/", UserLoginView.as_view, name="user_login"),
]

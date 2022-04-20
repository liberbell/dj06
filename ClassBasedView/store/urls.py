from django.urls import path
from .views import IndexView, HomeView, BookDetailView
# from django.views.generic.base import TemplateView

app_name = "store"

urlpatterns = [
    path('index/', IndexView.as_view(), name="index"),
    path('home/<name>', HomeView.as_view(), name="home"),
    # path('home/', TemplateView.as_view(template_name="home.html"), name="home"),
    path('detail_book/<int:pk>', BookDetailView, name="detail_book"),
]

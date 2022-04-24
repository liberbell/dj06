from django.urls import path
from .views import IndexView, HomeView, BookDetailView, BookListView, BookCreateView, BookUpdateView, BookdeleteView, BookFormView
# from django.views.generic.base import TemplateView

app_name = "store"

urlpatterns = [
    path('index/', IndexView.as_view(), name="index"),
    path('home/<name>', HomeView.as_view(), name="home"),
    # path('home/', TemplateView.as_view(template_name="home.html"), name="home"),
    path('detail_book/<int:pk>', BookDetailView.as_view(), name="detail_book"),
    path('book_list/', BookListView.as_view(), name="book_list"),
    path('book_list/<name>', BookListView.as_view(), name="book_list"),
    path('add_book/', BookCreateView.as_view(), name="add_book"),
    path('edit_book/<int:pk>/', BookUpdateView.as_view(), name="edit_book"),
    path('delete_book/<int:pk>/', BookdeleteView.as_view(), name="delete_book"),
    path('book_form/', BookFormView.as_view(), name="book_form"),
]

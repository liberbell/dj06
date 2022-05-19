from django.urls import path
from .views import ProductListView, ProductDetailView, add_product

app_name = "stores"
urlpatterns = [
    path("product_list/", ProductListView.as_view(), name="product_list"),
    path("product_detail/<int:pk>", ProductDetailView.as_view(), name="product_detail"),
    path("add_product/<int:pk>", add_product.as_view(), name="add_product"),
]

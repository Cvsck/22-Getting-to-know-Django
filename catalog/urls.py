from django.urls import path
from .views import (
    home,  # ✅ Добавляем функцию `home`
    ProductDetailView,
    ProductCreateView,
    ProductUpdateView,
    ProductDeleteView,
    ContactsView,
    ProductByCategoryView,
)

app_name = "catalog"

urlpatterns = [
    path("", home, name="home"),
    path("product/<int:pk>/", ProductDetailView.as_view(), name="product_detail"),
    path("product/create/", ProductCreateView.as_view(), name="product_create"),
    path("product/<int:pk>/edit/", ProductUpdateView.as_view(), name="product_edit"),
    path(
        "product/<int:pk>/delete/", ProductDeleteView.as_view(), name="product_delete"
    ),
    path("contacts/", ContactsView.as_view(), name="contacts"),
    path(
        "products/category/<slug:slug>/",
        ProductByCategoryView.as_view(),
        name="products_by_category",
    ),
]

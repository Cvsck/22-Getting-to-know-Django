from django.urls import path
from .views import ProductListView, ProductDetailView, ProductCreateView, ProductUpdateView, ProductDeleteView, ContactsView

app_name = "catalog"

urlpatterns = [
    path("", ProductListView.as_view(), name="home"),
    path("product/<int:pk>/", ProductDetailView.as_view(), name="product_detail"),
    path("product/create/", ProductCreateView.as_view(), name="product_create"),
    path("product/<int:pk>/edit/", ProductUpdateView.as_view(), name="product_edit"),
    path("product/<int:pk>/delete/", ProductDeleteView.as_view(), name="product_delete"),
    path("contacts/", ContactsView.as_view(), name="contacts"),  # 🔹 Добавили маршрут для контактов
]

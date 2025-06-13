from django.shortcuts import render
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
    TemplateView,
)
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin  # ✅ Ограничение доступа
from .models import Product
from .forms import ProductForm


# ✅ Функция для рендеринга `home.html`
def home(request):
    products = Product.objects.all()  # ✅ Получаем все товары
    return render(request, "home.html", {"products": products})


class ProductListView(ListView):
    model = Product
    template_name = "products_list.html"
    context_object_name = "products"


class ProductDetailView(DetailView):
    model = Product
    template_name = "product_detail.html"
    context_object_name = "product"


class ProductCreateView(
    LoginRequiredMixin, CreateView
):  # ✅ Только авторизованные пользователи
    model = Product
    form_class = ProductForm
    template_name = "product_form.html"
    success_url = reverse_lazy("catalog:home")


class ProductUpdateView(
    LoginRequiredMixin, UpdateView
):  # ✅ Только авторизованные пользователи
    model = Product
    form_class = ProductForm
    template_name = "product_form.html"

    def get_success_url(self):
        return reverse_lazy("catalog:product_detail", kwargs={"pk": self.object.pk})


class ProductDeleteView(
    LoginRequiredMixin, DeleteView
):  # ✅ Только авторизованные пользователи
    model = Product
    template_name = "product_confirm_delete.html"
    success_url = reverse_lazy("catalog:home")


class ContactsView(TemplateView):
    template_name = "contacts.html"

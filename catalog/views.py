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
from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    PermissionRequiredMixin,
)  # ✅ Ограничение доступа
from .models import Product
from .forms import ProductForm


# ✅ Функция для рендеринга `home.html`
def home(request):
    products = Product.objects.all()
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

    def form_valid(self, form):
        form.instance.owner = (
            self.request.user
        )  # ✅ Автоматически привязываем владельца
        return super().form_valid(form)


class ProductUpdateView(
    LoginRequiredMixin, PermissionRequiredMixin, UpdateView
):  # ✅ Проверка прав
    model = Product
    form_class = ProductForm
    template_name = "product_form.html"
    permission_required = "catalog.can_unpublish_product"

    def has_permission(self):
        product = self.get_object()
        return self.request.user == product.owner or self.request.user.has_perm(
            "catalog.can_unpublish_product"
        )

    def get_success_url(self):
        return reverse_lazy("catalog:product_detail", kwargs={"pk": self.object.pk})


class ProductDeleteView(
    LoginRequiredMixin, PermissionRequiredMixin, DeleteView
):  # ✅ Проверка прав
    model = Product
    template_name = "product_confirm_delete.html"
    success_url = reverse_lazy("catalog:home")
    permission_required = "catalog.can_delete_any_product"

    def has_permission(self):
        product = self.get_object()
        return self.request.user == product.owner or self.request.user.has_perm(
            "catalog.can_delete_any_product"
        )


class ContactsView(TemplateView):
    template_name = "contacts.html"

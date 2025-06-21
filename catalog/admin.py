from django.contrib import admin
from django.contrib.auth import get_user_model
from .models import Product, Category

User = get_user_model()


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "category",
        "owner",
        "price",
        "status",
        "created_at",
        "updated_at",
    )
    search_fields = (
        "name",
        "category__name",
        "owner__username",
    )
    list_filter = ("category", "status", "created_at")


class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "slug")
    prepopulated_fields = {"slug": ("name",)}  # автоматически подставлять slug из name


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(User)

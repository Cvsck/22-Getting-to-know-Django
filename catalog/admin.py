from django.contrib import admin
from .models import Product, Category

class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "category", "price", "created_at", "updated_at")  # 🔹 Заменили `purchase_price` на `price`
    search_fields = ("name", "category__name")
    list_filter = ("category", "created_at")

admin.site.register(Product, ProductAdmin)
admin.site.register(Category)

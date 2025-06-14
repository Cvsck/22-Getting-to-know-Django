from django.contrib import admin
from django.contrib.auth import get_user_model  # ✅ Добавляем пользователей
from .models import Product, Category

User = get_user_model()  # ✅ Получаем модель пользователя


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "category",
        "owner",  # ✅ Добавляем отображение владельца
        "price",
        "status",  # ✅ Добавляем статус публикации
        "created_at",
        "updated_at",
    )
    search_fields = (
        "name",
        "category__name",
        "owner__username",
    )  # ✅ Поиск по владельцу
    list_filter = ("category", "status", "created_at")  # ✅ Фильтр по статусу


admin.site.register(Product, ProductAdmin)
admin.site.register(Category)
admin.site.register(User)  # ✅ Регистрируем пользователей в админке

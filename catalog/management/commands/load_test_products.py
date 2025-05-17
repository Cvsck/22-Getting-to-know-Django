from django.core.management.base import BaseCommand
from catalog.models import Product, Category

class Command(BaseCommand):
    help = "Добавляет тестовые продукты"

    def handle(self, *args, **kwargs):
        Product.objects.all().delete()  # Удаление всех данных

        category, created = Category.objects.get_or_create(name="Электроника", description="Техника и гаджеты")

        Product.objects.create(name="Смартфон", description="Современный смартфон", category=category, purchase_price=500.00)
        Product.objects.create(name="Ноутбук", description="Мощный ноутбук", category=category, purchase_price=1200.00)

        self.stdout.write(self.style.SUCCESS("Тестовые продукты добавлены!"))

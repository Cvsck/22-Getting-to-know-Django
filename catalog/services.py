from catalog.models import Product
from django.core.cache import cache


class ProductService:
    @staticmethod
    def get_by_category(category_slug):
        key = f"category_products_{category_slug}"
        products = cache.get(key)
        if products is None:
            products = list(Product.objects.filter(category__slug=category_slug))
            cache.set(key, products, timeout=300)  # кеш на 5 минут
        return products

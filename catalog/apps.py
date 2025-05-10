from django.apps import AppConfig


class CatalogConfig(AppConfig):  # Исправлено на логичное название 'CatalogConfig'
    default_auto_field = "django.db.models.BigAutoField"
    name = "catalog"

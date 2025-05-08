from django.urls import path
from .views import home, contacts

app_name = "catalog"

urlpatterns = [
    path("", home, name="home"),  # Главная страница без "/contacts/"
    path("contacts/", contacts, name="contacts"),  # Контакты остаются на своем месте
]

from django.urls import path
from .views import home, contacts

app_name = "catalog"

urlpatterns = [
    path("", home, name="Home"),
    path("contacts/", contacts, name="contacts"),
]

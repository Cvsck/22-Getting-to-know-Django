from django.urls import path
from django.views.generic import TemplateView

app_name = "catalog"

urlpatterns = [
    path("", TemplateView.as_view(template_name="home.html"), name="home"),
    path(
        "contacts/",
        TemplateView.as_view(template_name="contacts.html"),
        name="contacts",
    ),
    path(
        "catalog/", TemplateView.as_view(template_name="catalog.html"), name="catalog"
    ),
    path("orders/", TemplateView.as_view(template_name="orders.html"), name="orders"),
    path(
        "profile/", TemplateView.as_view(template_name="profile.html"), name="profile"
    ),
    path("logout/", TemplateView.as_view(template_name="logout.html"), name="logout"),
    path(
        "settings/",
        TemplateView.as_view(template_name="settings.html"),
        name="settings",
    ),
    path("help/", TemplateView.as_view(template_name="help.html"), name="help"),
]

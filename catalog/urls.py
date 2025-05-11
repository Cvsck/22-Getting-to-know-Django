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
]

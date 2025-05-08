from django.shortcuts import render


def home(request):
    return render(request, "catalog/Home.html")


def contacts(request):
    return render(request, "catalog/contacts.html")

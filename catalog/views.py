from django.shortcuts import render

def home(request):
    return render(request, "home.html")  # Изменили 'Home.html' на 'home.html'

def contacts(request):
    return render(request, "contacts.html")

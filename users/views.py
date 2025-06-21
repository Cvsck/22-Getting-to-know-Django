import os
from django.core.mail import send_mail
from django.urls import reverse
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.views import LoginView
from dotenv import load_dotenv  # ✅ Загружаем `.env`
from django.conf import settings  # ✅ Добавляем использование `settings`
from .forms import CustomUserCreationForm

# ✅ Загружаем переменные из `.env`
load_dotenv()


def register(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            login(request, user)

            # ✅ Отправка приветственного письма с email из `settings`
            send_mail(
                "Добро пожаловать!",
                f"Здравствуйте, {user.username}! Спасибо за регистрацию.",
                settings.EMAIL_HOST_USER,  # ✅ Теперь email загружается из `settings`
                [user.email],
                fail_silently=False,
            )

            return redirect(
                "/"
            )  # ✅ Исправлено: прямое перенаправление вместо `reverse("/")`
    else:
        form = CustomUserCreationForm()
    return render(request, "users/register.html", {"form": form})


class CustomLoginView(LoginView):
    template_name = "users/login.html"
    redirect_authenticated_user = True  # ✅ Теперь вход работает корректно

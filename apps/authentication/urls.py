"""
Module with urls for authentication app
"""

from django.urls import path, reverse_lazy
from django.contrib.auth.models import User
from django.views.generic.edit import CreateView
from django.contrib.auth import views as auth_views

from .forms import RegistrationForm

urlpatterns = [
    # Django generic view for register user
    path(
        "registration",
        CreateView.as_view(
            model=User,
            form_class=RegistrationForm,
            template_name="authentication/registration.html",
            success_url=reverse_lazy("login"),
        ),
        name="registration",
    ),
    # Django generic view for login
    path(
        "",
        auth_views.LoginView.as_view(
            template_name="authentication/login.html",
            next_page=reverse_lazy("yandex_files"),
            redirect_authenticated_user=True,
        ),
        name="login",
    ),
    # Django generic view for logout
    path("logout", auth_views.LogoutView.as_view(), name="logout"),
]

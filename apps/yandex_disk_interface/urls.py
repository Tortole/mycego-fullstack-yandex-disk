"""
Module with urls for Yandex Disk interface
"""

from django.urls import path

from .views import YandexFilesView


urlpatterns = [
    path("", YandexFilesView.as_view(), name="yandex_files"),
]

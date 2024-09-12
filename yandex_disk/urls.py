"""
URL configuration for yandex_disk project.
"""

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("apps.authentication.urls")),
    path("yandex-files", include("apps.yandex_disk_interface.urls")),
]

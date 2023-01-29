"""project URL Configuration
"""
from django.contrib import admin
from django.shortcuts import redirect
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", lambda req: redirect("/profile")),
    path("", include("app.urls")),
]

from django.urls import path
from app import views

urlpatterns = [
    path("profile", views.profile),
    path("history", views.history),
    path("contact", views.contact, name="contact"),
    path("success/", views.success, name="success"),
    path("pdf", views.generate_pdf),
]

from django.urls import path
from app import views

urlpatterns = [
    path("profile", views.profile),
    path("history", views.history),
    path("contact", views.contact),
    path("pdf", views.generate_pdf),
]

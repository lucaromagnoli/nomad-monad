from django.urls import path
from app import views

urlpatterns = [
    path("profile", views.profile, name="profile"),
    path("history", views.history, name="history"),
    path("contact", views.contact, name="contact"),
    path("success/", views.success, name="success"),
    path("pdf", views.generate_pdf),
]

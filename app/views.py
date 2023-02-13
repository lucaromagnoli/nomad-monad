import datetime

from django.http import HttpResponse
from rest_framework.mixins import (
    CreateModelMixin,
    ListModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
)
from rest_framework.permissions import BasePermission, SAFE_METHODS, IsAuthenticated
from rest_framework.viewsets import GenericViewSet

from app.models import Experience, Profile, Home
from project import settings
from .render import html_to_pdf
from .serializers import ExperienceSerializer, ProfileSerializer


class ReadOnly(BasePermission):
    def has_permission(self, request, view):
        return request.method in SAFE_METHODS


def generate_pdf(request):
    experiences = Experience.objects.all()
    pdf_url = settings.FRONTEND_URI
    context = {
        "experiences": experiences,
        "name": settings.MY_NAME,
        "company": settings.MY_COMPANY,
        "mobile": settings.MY_MOBILE,
        "address": settings.MY_ADDRESS,
        "personal_email": settings.MY_PERSONAL_EMAIL,
        "linkedin": settings.MY_LINKEDIN,
        "pdf_url": pdf_url,
    }
    pdf = html_to_pdf("pdf_template.html", context)
    response = HttpResponse(pdf, content_type="application/pdf")
    today = datetime.datetime.now()
    filename = f"{settings.MY_NAME}_CV_{today.date()}.pdf"
    response["Content-Disposition"] = f"attachment; filename={filename}"
    return response


class HomeViewSet(
    GenericViewSet,
    CreateModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
    ListModelMixin,
):
    """
    API endpoint that allows groups to be viewed or edited.
    """

    permission_classes = [IsAuthenticated | ReadOnly]
    queryset = Home.objects.all()
    serializer_class = ProfileSerializer


class ProfileViewSet(
    GenericViewSet,
    CreateModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
    ListModelMixin,
):
    """
    API endpoint that allows groups to be viewed or edited.
    """

    permission_classes = [IsAuthenticated | ReadOnly]
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


class ExperienceViewSet(
    GenericViewSet,
    CreateModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
    ListModelMixin,
):
    """
    API endpoint that allows groups to be viewed or edited.
    """

    permission_classes = [IsAuthenticated | ReadOnly]
    queryset = Experience.objects.all()
    serializer_class = ExperienceSerializer

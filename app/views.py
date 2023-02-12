from django.http import HttpResponse
from rest_framework.mixins import (
    CreateModelMixin, ListModelMixin, RetrieveModelMixin, UpdateModelMixin
)
from rest_framework.permissions import BasePermission, SAFE_METHODS, IsAuthenticated
from rest_framework.viewsets import GenericViewSet

from app.models import Experience
from .render import html_to_pdf
from .serializers import ExperienceSerializer


class ReadOnly(BasePermission):
    def has_permission(self, request, view):
        return request.method in SAFE_METHODS

def generate_pdf(request):
    experiences = Experience.objects.all()
    context = {"experiences": experiences, "url": request.build_absolute_uri()}
    pdf = html_to_pdf("pdf_template.html", context)
    return HttpResponse(pdf, content_type="application/pdf")


class ExperienceViewSet(GenericViewSet, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, ListModelMixin):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    permission_classes = [IsAuthenticated|ReadOnly]
    queryset = Experience.objects.all()
    serializer_class = ExperienceSerializer

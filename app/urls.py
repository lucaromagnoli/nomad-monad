from django.urls import path, include
from rest_framework import routers

from app import views

router = routers.DefaultRouter()
router.register(r'experiences', views.ExperienceViewSet)


urlpatterns = [
    path('api/', include(router.urls)),
    path('', include('rest_framework.urls', namespace='rest_framework')),
    path("pdf/", views.generate_pdf, name="pdf"),
]
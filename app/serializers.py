from rest_framework import serializers

from app.models import Experience


class ExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"
        model = Experience

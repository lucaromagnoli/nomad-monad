from rest_framework import serializers

from app.models import Experience, Profile


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"
        model = Profile


class ExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"
        model = Experience

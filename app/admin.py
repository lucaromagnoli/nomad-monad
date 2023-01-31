from django.contrib import admin

from app.models import Experience


@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    pass

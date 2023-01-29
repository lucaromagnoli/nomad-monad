from django.db import models


class Experience(models.Model):
    company_name = models.CharField(max_length=30)
    company_url = models.CharField(max_length=30)
    start_date = models.DateField()
    end_date = models.DateField()
    role = models.CharField(max_length=30)
    description = models.TextField()
    tech = models.JSONField()

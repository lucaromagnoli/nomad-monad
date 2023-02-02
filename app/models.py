import datetime

from django.db import models


class Experience(models.Model):
    company_name = models.CharField(max_length=30)
    company_url = models.CharField(max_length=30)
    start_date = models.DateField()
    end_date = models.DateField()
    role = models.CharField(max_length=30)
    description = models.TextField()
    technologies: dict = models.JSONField(blank=True, null=True)

    class Meta:
        ordering = ["-start_date"]

    def __str__(self):
        return f"{self.role}@{self.company_name} {self.period}"

    @property
    def period(self) -> str:
        start = self.start_date.strftime("%b %Y")
        if self.end_date == datetime.datetime.now().date():
            end = "present"
        else:
            end = self.end_date.strftime("%b %Y")
        return f"{start} to {end}"

    @property
    def tech_stack(self):
        sorted_items = sorted(self.technologies.items(), key=lambda tech: tech[1]["order"])
        for tech_item in sorted_items:
            tech_name, tech_config = tech_item
            yield tech_name, tech_config.get("libraries", [])

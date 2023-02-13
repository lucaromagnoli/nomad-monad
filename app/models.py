import datetime
import uuid

from django.db import models


class SingletonModel(models.Model):
    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        self.pk = 1
        super(SingletonModel, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        pass

    @classmethod
    def load(cls):
        obj, created = cls.objects.get_or_create(pk=1)
        return obj


class BaseSection(SingletonModel):
    text: str = models.TextField()
    images: list = models.JSONField(blank=True, null=True)
    links: list = models.JSONField(blank=True, null=True)


class Home(BaseSection):
    """Home Section"""

    def __str__(self):
        return "Home"


class Profile(BaseSection):
    """Profile Section"""

    def __str__(self):
        return "Profile"


class Experience(models.Model):
    """Work Section"""

    unique_id = models.UUIDField(primary_key=False, default=uuid.uuid4, editable=False)
    company_name: str = models.CharField(max_length=30)
    company_url: str = models.CharField(max_length=30)
    start_date: datetime.date = models.DateField()
    end_date: datetime.date = models.DateField()
    role: str = models.CharField(max_length=30)
    description: str = models.TextField()
    technologies: list = models.JSONField(blank=True, null=True)

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
        sorted_items = sorted(self.technologies, key=lambda tech: tech["order"])
        for tech_item in sorted_items:
            tech_name, tech_config = tech_item
            yield tech_name, tech_config.get("libraries", [])

    @property
    def tech_stack_as_string(self):
        sorted_items = sorted(self.technologies, key=lambda tech: tech["order"])
        for tech_item in sorted_items:
            tech_name, tech_config = tech_item
            yield tech_name, " ".join(tech_config.get("libraries", []))

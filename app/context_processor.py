import datetime

import django
import django_bootstrap5.core


def get_bootstrap_version():
    version = ""
    url = django_bootstrap5.core.css_url()["url"]
    parts = url.split("/")
    for part in parts:
        if "@" in part:
            name, version = part.split("@")
            return version


def context_processor(request):
    context = dict()
    context["django_url"] = "https://www.djangoproject.com/"
    context["django_version"] = f"Django {django.get_version()}"
    context["bootstrap_url"] = "https://getbootstrap.com/"
    context["bootstrap_version"] = f"Bootstrap {get_bootstrap_version()}"
    context["repo_url"] = "https://github.com/lucaromagnoli/resume"
    context["site_url"] = ""
    context["site_name"] = "Luca Romagnoli"
    context["copyright_year"] = datetime.datetime.now().year
    return context

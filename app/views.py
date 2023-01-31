from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from django.views.generic import View

from app.models import Experience
from .render import html_to_pdf


def profile(request):
    template = loader.get_template("profile.html")
    return HttpResponse(template.render({}, request))


def history(request):
    template = "history.html"
    experiences = Experience.objects.all()
    context = {"experiences": experiences}
    return render(request, template, context)


def generate_pdf(request):
    experiences = Experience.objects.all()
    context = {"experiences": experiences}
    pdf = html_to_pdf('history.html', context)
    return HttpResponse(pdf, content_type='application/pdf')


from django.http import HttpResponse
from django.template import loader


def profile(request):
    template = loader.get_template("profile.html")
    return HttpResponse(template.render({}, request))


def history(request):
    template = loader.get_template("profile.html")
    return HttpResponse(template.render({}, request))

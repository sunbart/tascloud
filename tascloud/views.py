from django.http import HttpResponse
from django.template.loader import render_to_string


def index(request):
    return HttpResponse(render_to_string("tascloud/index.html"))

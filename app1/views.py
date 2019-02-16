from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.sites.shortcuts import get_current_site


# Create your views here.
def index(request):
    csite = get_current_site(request)
    csite.name
    html = "<h1>{}</h1>".format(
        csite.name
    )
    return HttpResponse(html)

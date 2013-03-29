from django.http import Http404
from django.http import HttpResponse
from django.shortcuts import render_to_response

def staticpage(request, page_name):
    # Use some exception handling, just to be safe
    try:
        return render_to_response('%s.html' % (page_name, ))
    except TemplateDoesNotExist:
        raise Http404# Create your views here.

def home(request):
    return render_to_response("home.html")
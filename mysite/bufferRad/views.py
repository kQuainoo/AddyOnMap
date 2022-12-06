from django.shortcuts import render
from django.http.response import Http404
from django.utils import timezone

from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.template.context import ContextDict

from .models import UserRadius

def index(request):
    database_display = UserRadius.objects.order_by('city')
    template = loader.get_template('bufferRad/index.html')
    context = {
        'database_display': database_display
    }
    return HttpResponse(template.render(context,request))
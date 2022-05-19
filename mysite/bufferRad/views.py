from django.shortcuts import render
from django.http.response import Http404
from django.views import generic

from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.template.context import ContextDict


# import models.


# Create your views here.

class IndexView(generic.ListView):
    template_name = 'bufferRad/index.html'
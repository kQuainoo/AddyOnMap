from django.shortcuts import render
from django.http.response import Http404
from django.views import generic
from django.utils import timezone

from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.template.context import ContextDict

from .models import UserRadius


# import models.


# Create your views here.

class IndexView(generic.ListView):
    template_name = 'bufferRad/index.html'

    def get_queryset(self):

        return UserRadius.objects.filter(
            pub_date__lte= timezone.now()
        )
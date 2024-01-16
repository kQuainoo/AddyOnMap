from django.shortcuts import render
from django.http.response import Http404
from django.utils import timezone

from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.template.loader import get_template
from django.template.context import ContextDict
from django.views.generic import TemplateView, DetailView, FormView

from django import forms

from .models import UserRadius


class IndexView(FormView):
    template_name = 'index.html'
    form_class = 'AddyInputForm'
    success_url = 'bufferRad/index.html'

    def get_context_data(self, form) -> dict[str,var]:
        context = 'dosomething'
        return super().get_context_data(form)
    

    def form_valid(self, form) -> HttpResponse:

        return super(IndexView).form_valid(form)




class DetailView(generic.DetailView):
    model = UserRadius
    template_name = 'bufferRad/index.html'

    def get_queryset(self):
        ''' what this does is..'''
        return UserRadius.objects.count()

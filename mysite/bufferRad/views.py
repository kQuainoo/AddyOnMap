from django.shortcuts import render
from django.http.response import Http404
from django.utils import timezone

from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.template.loader import get_template
from django.template.context import ContextDict
from django.views import generic
from django.views.generic import TemplateView, DetailView



from .models import UserRadius



# def index(request):

#     template = loader.get_template('bufferRad/index.html')
#     return render(request,'bufferRad/index.html')

# def post(self,request):

#     return 

class IndexView(generic.TemplateView):
    template_name = 'index.html'
    # context_object_name = 'somethingoeshere'

    # def get_queryset(self):
    #     return UserRadius.objects.count

class DetailView(generic.DetailView):
    model = UserRadius
    template_name = 'bufferRad/index.html'

    def get_queryset(self):
        ''' what this does is..'''
        return UserRadius.objects.count()

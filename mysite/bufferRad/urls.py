from django.urls import path
from django.views.generic import TemplateView


from . import views

# this py script will create UrlConfig

app_name = 'bufferRad'

urlpatterns = [
    path('', TemplateView.as_view(template_name = 'index.html')),
    path('<int:pk>/',views.TemplateView.as_view(template_name ='index.html')),
    
]
# tuple urlpatterns. is ordered and unchangable collection of items and allow duplicates
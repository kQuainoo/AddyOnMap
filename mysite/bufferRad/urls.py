from django.urls import path

from . import views

# this py script will create UrlConfig
app_name = 'bufferRad'
urlpatterns = [
    path('', views.index, name = 'index')
]

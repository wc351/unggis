from django.conf.urls import patterns, include, url
from geoapi import views

urlpatterns = patterns('',
    url(r'^', include('geoapi.api_urls')),
    )

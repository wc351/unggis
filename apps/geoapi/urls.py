from django.conf.urls import patterns, include, url
from apps.geoapi import views

urlpatterns = patterns('',
    url(r'^', include('apps.geoapi.api_urls')),
    )

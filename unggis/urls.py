from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',

    url(r'^admin/', include(admin.site.urls)),
    url(r'^geoapi/', include('geoapi.urls', namespace='geoapi')),
    )

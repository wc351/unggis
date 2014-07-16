from django.conf.urls import patterns, include, url
from geoapi.json_views import CallBoxCollection, SingleCallBoxCollection


urlpatterns = patterns('',
    # Examples:
    url(r'^v1/callboxes$', CallBoxCollection.as_view(), name='callbox_collection'),
    url(r'^v1/callboxes/(?P<pk>[0-9]+)$', SingleCallBoxCollection.as_view(), name='single_cb_collection'),
)
from django.conf.urls import patterns, include, url
from apps.geoapi import json_views


urlpatterns = patterns('',
    # Examples:
    url(r'^v1/callboxes$', json_views.CallBoxCollection.as_view(), name='callbox_collection'),
    url(r'^v1/callboxes/(?P<pk>[0-9]+)$', json_views.SingleCallBoxCollection.as_view(), name='single_cb_collection'),

    url(r'^v1/lamps$', json_views.LampCollection.as_view(), name='lamp_collection'),
    url(r'^v1/lamps/(?P<pk>[0-9]+)$', json_views.SingleLampCollection.as_view(), name='single_lamp_collection'),

    url(r'^v1/secure/lamps$', json_views.SecureLampCollection.as_view(), name='secure_lamp_collection'),
    url(r'^v1/secure/lamps/(?P<pk>[0-9]+)$', json_views.SecureSingleLampCollection.as_view(), name='secure_single_lamp_collection'),

    url(r'^v1/parkinglots$', json_views.ParkingLotCollection.as_view(), name='parkinglot_collection'),
    url(r'^v1/parkinglots/(?P<pk>[0-9]+)$', json_views.SingleParkingLotCollection.as_view(),
        name='single_parkinglot_collection'),

)
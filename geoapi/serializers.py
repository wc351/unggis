from rest_framework_gis import serializers
from geoapi import models


class CBSerializer(serializers.GeoFeatureModelSerializer):
    class Meta:
        model = models.CallBox
        geo_field = "geom"
        fields = ('id', 'description',)
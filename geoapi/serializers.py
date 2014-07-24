from rest_framework_gis import serializers
from geoapi import models


class CBSerializer(serializers.GeoFeatureModelSerializer):
    class Meta:
        model = models.CallBox
        geo_field = "geom"
        fields = ('id', 'description',)


class LampSerializer(serializers.GeoFeatureModelSerializer):
    class Meta:
        model = models.Lamp
        geo_field = "geom"
        fields = ('id', 'light_type', 'heads')


class ParkingLotSerializer(serializers.GeoFeatureModelSerializer):
    class Meta:
        model = models.ParkingLot
        geo_field = "geom"
        fields = ('id', 'lot_name', 'description')
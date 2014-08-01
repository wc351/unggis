from rest_framework_gis import serializers
from apps.geoapi import models


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


class SecureLampSerializer(serializers.GeoFeatureModelSerializer):
    class Meta:
        model = models.SecureLamp
        geo_field = "geom"
        fields = ('id', 'light_type', 'heads', 'id_no', 'building', 'panel', 'breaker', 'zone', 'max_pdop', 'max_hdop',
                   'corr_type', 'vert_perc', 'horz_perc', 'std_dev', 'light_radius', 'dark_radius', 'intensity')


class ParkingLotSerializer(serializers.GeoFeatureModelSerializer):
    class Meta:
        model = models.ParkingLot
        geo_field = "geom"
        fields = ('id', 'lot_name', 'description')
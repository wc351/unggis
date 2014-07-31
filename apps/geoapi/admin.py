from django.contrib.gis import admin
from apps.geoapi import models

admin.site.register(models.CallBox)
admin.site.register(models.Lamp)
admin.site.register(models.ParkingLot)


from django.contrib.gis.db import models


class CallBox(models.Model):
    description = models.CharField(max_length=140)
    geom = models.PointField()
    objects = models.GeoManager()

    class Meta:
        verbose_name = 'CallBox'
        verbose_name_plural = 'CallBoxes'

    def __str__(self):
        return self.description


class Lamp(models.Model):

# look up field.choices on the djangoproject docs site
    FLOOD = 'FL'
    RADIAL = 'RD'
    LAMP_CHOICES = ((FLOOD, 'Flood'),
                    (RADIAL, 'Radial')
                    )
    light_type = models.CharField(max_length=2, choices=LAMP_CHOICES)
    heads = models.IntegerField()
    geom = models.PointField()
    objects = models.GeoManager()

    class Meta:
        verbose_name = 'Lamp'
        verbose_name_plural = 'Lamps'

    def __str__(self):
        return self.light_type


class ParkingLot(models.Model):
    lot_name = models.CharField(max_length=5)
    description = models.CharField(max_length=150)
    geom = models.MultiPolygonField()
    objects = models.GeoManager()

    class Meta:
        verbose_name = 'Parking_Lot'
        verbose_name_plural = 'Parking_Lots'

    def __str__(self):
        return self.lot_name
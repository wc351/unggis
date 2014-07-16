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
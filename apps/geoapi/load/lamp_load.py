import shapefile
from apps.geoapi import models
import django
django.setup()



lamp_path = 'U:/Shared/GIS/Projects/JZM_2013_2014/unggis/data/UNGGainesvilleLampData/LampData.shp'

sf = shapefile.Reader(lamp_path)
sr = sf.shapeRecords()
lamp_choices = {'Flood': 'FL', 'Radial': 'RD'}

for r in sr:
    m = models.SecureLamp(id_no=r.record[0], light_type=lamp_choices[r.record[1]], heads=r.record[2],
               building=r.record[3], panel=r.record[4], breaker=r.record[5],
               zone=r.record[6], max_pdop=r.record[7], max_hdop=r.record[8],
               corr_type=r.record[9], vert_perc=r.record[10], horz_perc=r.record[11],
               std_dev=r.record[12], light_radius=r.record[13], dark_radius=r.record[14],
               intensity=r.record[15],
               geom="POINT({} {})".format(r.shape.points[0][0], r.shape.points[0][1]))
    print(r.record[0], r.record[1], r.record[2], r.record[3], r.record[4],
          r.record[5], r.record[6], r.record[7], r.record[8], r.record[9],
          r.record[10], r.record[11], r.record[12], r.record[13], r.record[14],
          r.record[15], r.shape.points)
    m.save()
from django.contrib.gis.db import models


class Jog(models.Model):
    start = models.DateTimeField()
    end = models.DateTimeField()


class Datapoint(models.Model):
    jog = models.ForeignKey(Jog, db_index=True)
    coordTime = models.DateTimeField()
    coord = models.PointField()

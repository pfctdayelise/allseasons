from django.db import models
from geoposition.fields import GeopositionField


class EventOfInterest(models.Model):
    name = models.CharField(max_length=100)
    location = GeopositionField()
    date = models.DateField()

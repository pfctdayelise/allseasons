import datetime
from django.db import models
from geoposition.fields import GeopositionField

default_date = datetime.date(2000, 7, 15)


class EventOfInterest(models.Model):
    name = models.CharField(max_length=100)
    location = GeopositionField()
    date = models.DateField(default=default_date)
    seasonset = models.CharField(max_length=100)

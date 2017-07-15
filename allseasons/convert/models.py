import datetime
from django.db import models
from geoposition.fields import GeopositionField
import seasons

default_date = datetime.date(2000, 7, 15)


class EventOfInterest(models.Model):
    name = models.CharField(max_length=100)
    location = GeopositionField()
    date = models.DateField(default=default_date)
    seasonset = models.CharField(max_length=100)

    def __unicode__( self ):
        return "{0.name} {0.location} {0.date} {0.seasonset}".format(self)

    @property
    def season(self):
        try:
            seasonset = [ss for ss in seasons.season_sets
                         if ss.name == self.seasonset][0]
            return seasonset.get_season(self.date)
        except IndexError:
            return 'Error'

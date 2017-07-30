import datetime
from django.db import models
from geoposition.fields import GeopositionField
import seasons

default_date = datetime.date(2000, 7, 15)


class EventOfInterest(models.Model):
    name = models.CharField(max_length=100)
    location = GeopositionField()
    date = models.DateField(default=default_date)
    calendar = models.CharField(max_length=100)

    def __str__( self ):
        return "{0.name} {0.location} {0.date} {0.calendar}".format(self)

    @property
    def season(self):
        try:
            calendar = [c for c in seasons.calendars
                        if c.name == self.calendar][0]
            return calendar.get_season(self.date)
        except IndexError:
            return 'Error'

    def format_html(self):
        s = '''The event of <i>{0.name}</i>,
which occurred on {0.date}
at {0.location},
according to the {0.calendar} calendar
fell during the season of <b>{0.season}</b>!'''
        return s.format(self)

    def format_plaintext(self):
        s = '''The event of "{0.name}",
which occurred on {0.date}
at {0.location},
according to the {0.calendar} calendar
fell during the season of ***{0.season}***!'''
        return s.format(self)

    def format_short(self):
        s = 'DYK? "{0.name}" = season {0.season}!'
        return s.format(self)


class Message(models.Model):

    MESSAGE_CHOICES = [('email', 'email')]
    
    sender = models.CharField(max_length=100)
    receiver = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now=True)
    message_type = models.CharField(choices=MESSAGE_CHOICES, max_length=100)
    event = models.ForeignKey(EventOfInterest, on_delete=models.CASCADE)

    def __str__(self):
        return "{0.from_} {0.to} {0.date}".format(self)

    class Meta:
        ordering = ('date',)

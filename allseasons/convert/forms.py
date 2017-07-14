from django import forms
from django.forms.extras.widgets import SelectDateWidget
from .models import EventOfInterest


class EventForm(forms.ModelForm):

    class Meta:
        model = EventOfInterest
        fields = ('name', 'date', 'location',)
        widgets = {
            'date': SelectDateWidget,
        }

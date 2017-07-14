from django import forms
from django.forms.extras.widgets import SelectDateWidget
from .models import EventOfInterest



class EventForm1(forms.ModelForm):
    class Meta:
        model = EventOfInterest
        fields = ('name', 'date', 'location',)
        widgets = {
            'date': SelectDateWidget(years=range(1900, 2030)),
        }


class EventForm2(forms.ModelForm):
    class Meta:
        model = EventOfInterest
        fields = ('seasonset', )

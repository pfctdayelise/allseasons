from django import forms
from django.forms.extras.widgets import SelectDateWidget
from .models import EventOfInterest, Message


class EventForm(forms.ModelForm):
    class Meta:
        model = EventOfInterest
        fields = ('name', 'date', 'location', 'calendar')


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
        fields = ('calendar', )
        widgets = {
            'calendar': forms.RadioSelect,
        }


class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ('sender', 'receiver', 'message_type')
        widgets = {
            'message_type': forms.RadioSelect,
        }

from django import forms

from .models import PointOfInterest

class PlaceForm(forms.ModelForm):

    class Meta:
        model = PointOfInterest
        fields = ('name', 'position',)

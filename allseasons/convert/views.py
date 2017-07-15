from django.shortcuts import render, redirect, get_object_or_404
from .forms import EventForm, EventForm1, EventForm2
from .models import EventOfInterest


def result(request, pk):
    event = get_object_or_404(EventOfInterest, pk=pk)
    print(event)
    return render(request, 'result.html', {'event': event})


def index(request):
    if request.method == 'POST':
        form = EventForm1(request.POST)
        if form.is_valid():
            event = form.save(commit=False)
            event.save()
            return redirect('result', pk=event.pk)

    form = EventForm1()
    return render(request, 'newform.html', {'form': form})



from django.http import HttpResponseRedirect
from formtools.wizard.views import SessionWizardView
from django import forms
from geoposition.fields import GeopositionField
import seasons


class EventWizard(SessionWizardView):
    template_name = 'newform.html'
    form_list = (EventForm1, EventForm2)

    def get_form(self, step=None, data=None, files=None):
        form = super(EventWizard, self).get_form(step, data, files)

        # determine the step if not given
        if step is None:
            step = self.steps.current

        if step == '1':
            location = self.get_cleaned_data_for_step('0')['location']
            ssets = seasons.get_valid_seasonsets(seasons.Location(*location))
            choices = [(ss.name, ss.name) for ss in ssets]
            form.fields['seasonset'] = forms.ChoiceField(choices=choices,
                                                         widget=forms.RadioSelect)

        return form

    def done(self, form_list, **kwargs):
        assert all(form.is_valid() for form in form_list)
        form_data = self.get_all_cleaned_data()
        form_data['location'] = '{}, {}'.format(*[l for l in form_data['location']])
        event = EventOfInterest(**form_data)
        event.save()
        return redirect('result', pk=event.pk)

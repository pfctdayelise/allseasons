import datetime
from formtools.wizard.views import SessionWizardView
from django import forms
import seasons
import location
from django.shortcuts import render, redirect, get_object_or_404
from .forms import EventForm, EventForm1, EventForm2, MessageForm
from .models import EventOfInterest, Message
from django.core.mail import send_mail


def send(request, pk):
    message = get_object_or_404(Message, pk=pk)
    if message.mtype == 'email':
        subj = 'Some important season information!'
        body = message.event.format_plaintext()
        send_mail(subj, body, message.sender, [message.receiver], fail_silently=False)
        # Possible errors raised here:
        #    ConnectionRefusedError
        #    SMTPServerDisconnected
        message.date = datetime.datetime.utcnow()
        message.save()

    return render(request, 'send.html', {'message': message})


def result(request, pk):
    event = get_object_or_404(EventOfInterest, pk=pk)

    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.event = event
            message.save()
            return redirect('send', pk=message.pk)

    form = MessageForm()
    return render(request, 'result.html', {'event': event, 'form': form})


class EventWizard(SessionWizardView):
    template_name = 'newform.html'
    form_list = (EventForm1, EventForm2)

    def get_form(self, step=None, data=None, files=None):
        form = super(EventWizard, self).get_form(step, data, files)

        # determine the step if not given
        if step is None:
            step = self.steps.current

        if step == '1':
            latlng = self.get_cleaned_data_for_step('0')['location']
            calendars = seasons.get_valid_calendars(location.Location(*latlng))
            choices = [(c.name, c.name) for c in calendars]
            form.fields['calendar'] = forms.ChoiceField(choices=choices,
                                                        widget=forms.RadioSelect)

        return form

    def done(self, form_list, **kwargs):
        assert all(form.is_valid() for form in form_list)
        form_data = self.get_all_cleaned_data()
        form_data['location'] = '{}, {}'.format(*[l for l in form_data['location']])
        event = EventOfInterest(**form_data)
        event.save()
        return redirect('result', pk=event.pk)

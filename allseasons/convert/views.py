from django.shortcuts import render, redirect, get_object_or_404
from .forms import EventForm1, EventForm2
from .models import EventOfInterest


def result(request, pk):
    event = get_object_or_404(EventOfInterest, pk=pk)
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

class EventWizard(SessionWizardView):
    template_name = 'newform.html'
    form_list = (EventForm1, EventForm2)

    def done(self, form_list, **kwargs):
        do_something_with_the_form_data(form_list)
        return HttpResponseRedirect('/page-to-redirect-to-when-done/')

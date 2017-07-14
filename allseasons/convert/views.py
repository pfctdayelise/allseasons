from django.shortcuts import render, redirect, get_object_or_404
from .forms import EventForm
from .models import EventOfInterest


def result(request, pk):
    event = get_object_or_404(EventOfInterest, pk=pk)
    return render(request, 'result.html', {'event': event})


def index(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            event = form.save(commit=False)
            event.save()
            return redirect('result', pk=event.pk)

    form = EventForm()
    return render(request, 'newform.html', {'form': form})

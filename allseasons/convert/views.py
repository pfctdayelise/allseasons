from django.shortcuts import render
from .forms import EventForm


def index_old(request):
    
    return render(request, 'base.html', {'content': 'Hello, world',
                                         'title': 'convert',
    })


def index(request):
    form = EventForm()
    return render(request, 'base.html', {'form': form})

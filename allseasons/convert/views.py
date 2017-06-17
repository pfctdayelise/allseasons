from django.shortcuts import render
from .forms import PlaceForm


def index_old(request):
    
    return render(request, 'base.html', {'content': 'Hello, world',
                                         'title': 'convert',
    })


def index(request):
    form = PlaceForm()
    return render(request, 'base.html', {'form': form})

from datetime import date
from django.shortcuts import render
from django.http import HttpResponse
from events.models import Event

def index(request):
    current_events=Event.objects.filter(dt='1999-01-01')
    context={
        'current_events':current_events
    }
    return render(request, 'index.html',context=context)
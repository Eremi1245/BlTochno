from datetime import date
from django.shortcuts import render
from django.http import HttpResponse
from events.models import Event

def index(request):
    today_events=Event.objects.all().filter(dt=date.today())
    context={
        'today_events':today_events
    }
    return render(request, 'index.html',context=context)
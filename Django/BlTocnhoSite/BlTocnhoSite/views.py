from datetime import date, datetime
from django.shortcuts import render
from django.http import HttpResponse
from events.models import Event
from events.view.event import get_all_events

def index(request):
    current_events=Event.objects.filter(dt='1999-01-01')
    today=datetime.today().date().strftime("%Y-%m-%d")
    today_events=get_all_events(dt=today)
    context={
        'current_events':current_events,
        "today_events":today_events,
        'date_string':today,
        'title':'Dashboard'
    }
    # return render(request, 'index.html',context=context)
    return render(request, 'bootstrap_main/index.html',context=context)
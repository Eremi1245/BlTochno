import datetime
from django.shortcuts import render
from django.http import HttpResponse

def calendar(request):
    return render(request, 'calendar/calendar.html')



def event(request,event_id):
    print(event_id)
    return render(request, 'calendar/event_list.html')
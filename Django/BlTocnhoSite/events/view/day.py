from django.shortcuts import render
from events.view.event import get_all_events


def events_day(request, date_string):
    events = get_all_events(date_string)
    context = {
        'events': events,
        'date_string': date_string
    }
    return render(request, 'calendar/day/day_card.html', context=context)
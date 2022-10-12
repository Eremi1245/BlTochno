from collections import defaultdict
from datetime import date, datetime, time, timedelta

import requests
from django.shortcuts import render
from django.http import HttpResponse

from events.models import Event

from secret import home_url

today = date.today()
my_year = today.year
my_month = today.month
my_day = today.day


def calendar(request, year: int = None, month: int = None):
    if not year:
        year = my_year
    if not month:
        month = my_month
    month_list = calendar_builder(year, month)
    month_dict = days_to_events(month_list)
    if month == 12:
        next_year = year + 1
        prev_year = year
        next_month = 1
        prev_month = month - 1
    elif month == 1:
        prev_year = year - 1
        prev_month = 12
        next_year = year
        next_month = month + 1
    else:
        next_year = year
        prev_year = year
        next_month = month + 1
        prev_month = month - 1
    context = {
        'month_list': month_dict,
        'year': year,
        'next_year': next_year,
        'prev_year': prev_year,
        'month': month,
        'prev_month': prev_month,
        'next_month': next_month
    }
    return render(request, 'calendar/calendar.html', context=context)

def event(request, event_id):
    return render(request, 'calendar/event_list.html')

def get_all_events(dt: date):
    day_events = Event.objects.all().filter(dt=dt).order_by('tm')
    if len(day_events) == 0:
        return day_events
    curr_hour = datetime(year=datetime.now().year,month=datetime.now().month,day=datetime.now().day,hour=datetime.now().hour)
    for event in day_events:
        event_date_hour=datetime(year=event.dt.year,month=event.dt.month,day=event.dt.day,hour=event.tm.hour)
        if event_date_hour == curr_hour:
            Event.objects.filter(pk=event.id).update(status='In processing')
        elif event_date_hour < curr_hour:
            Event.objects.filter(pk=event.id).update(status='passed')
        else:
            break
    query_set = Event.objects.all().filter(dt=dt).order_by('tm')
    return query_set

def days_to_events(month: list[list[date]]) -> dict[date:list[Event]]:
    events_list = []
    for week in month:
        week_events = []
        for day in week:
            day_dict = dict()
            day_dict['day'] = day
            day_dict['weekday'] = int_to_weekday(day.weekday())
            day_dict['events'] = get_all_events(day)
            week_events.append(day_dict)
        events_list.append(week_events)
    return events_list

def calendar_builder(year: int = None, month: int = None) -> list[list[date]]:
    start_day = date(year, month, 1)
    if month == 12:
        year = year + 1
        month = 1
    end_day = date(year, month + 1, 1) - timedelta(days=1)
    start_day = start_day - timedelta(days=start_day.weekday())
    month = []
    index = 1
    while start_day <= end_day:
        week = ['', '', '', '', '', '', '']
        for day_index in range(7):
            week[start_day.weekday()] = start_day
            if start_day.weekday() == 6:
                break
            else:
                start_day += timedelta(days=1)
                continue
        month.append(week)
        start_day += timedelta(days=1)
        index += 1
    return month

def int_to_weekday(weekday: int):
    if weekday == 0:
        weekday = 'Понедельник'
    elif weekday == 1:
        weekday = 'Вторник'
    elif weekday == 2:
        weekday = 'Среда'
    elif weekday == 3:
        weekday = 'Четверг'
    elif weekday == 4:
        weekday = 'Пятница'
    elif weekday == 5:
        weekday = 'Суббота'
    elif weekday == 6:
        weekday = 'Воскресенье'
    return weekday

def events_day(request, date_string):
    events = get_all_events(date_string)
    context = {
        'events': events,
        'date_string':date_string
    }
    return render(request, 'calendar/day_card.html', context=context)

def event_action(request,id,action):
    resp=requests.post(home_url+f'api/events/{id}/{action}').status_code
    print(resp)
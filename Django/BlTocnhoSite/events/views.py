from collections import defaultdict
from datetime import date, datetime, time, timedelta
from queue import Empty
from django.views.decorators.csrf import csrf_exempt
import json
import requests
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from events.forms import AddEventForm, AddCategoryForm,EditCategoryForm
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from events.models import Event, Category, Habit, Habits_Events

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
    event=get_object_or_404(Event, id=event_id)
    if request.method == 'POST':
        event_form = AddEventForm(request.POST, instance=event)

        if event_form.is_valid():
            updt_event = event_form.save(commit=False)
            updt_event.save()

            return redirect('event',event.id)
        else:
            return HttpResponse(event_form.errors)
    else:
        event_form = AddEventForm(instance=event)
    return render(request, 'calendar/event_card.html', {'event_form': event_form,'event':event})


def get_all_events(dt: date):
    day_events = Event.objects.filter(dt=dt).order_by('tm')
    if len(day_events) == 0:
        return day_events
    curr_hour = datetime(year=datetime.now().year, month=datetime.now(
    ).month, day=datetime.now().day, hour=datetime.now().hour)
    for event in day_events:
        event_date_hour = datetime(
            year=event.dt.year, month=event.dt.month, day=event.dt.day, hour=event.tm.hour)
        if event_date_hour == curr_hour and event.status == 'ACTIVE':
            Event.objects.filter(pk=event.id).update(status='In processing')
        elif event_date_hour < curr_hour and event.status == 'ACTIVE':
            Event.objects.filter(pk=event.id).update(status='passed')
        else:
            break
    query_set = Event.objects.filter(dt=dt).order_by('tm')
    query_set = list(filter(lambda day: day.status != 'CANCEL', query_set))
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
        end_day=date(year, month, 31)
    else:
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
        'date_string': date_string
    }
    return render(request, 'calendar/day_card.html', context=context)


def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'


def parse_body(request):
    body_unicode = request.body.decode('utf-8').split('&')
    body_unicode = [item.split('=') for item in body_unicode]
    body = {k: v for k, v in body_unicode}
    return body


def event_action(request):
    if request.method == "POST" and is_ajax(request=request):
        body = parse_body(request=request)
        try:
            if body['action'] == 'CANCEL':
                Event.objects.filter(pk=body['id']).delete()
                return JsonResponse({"success": True}, status=200)
            else:
                Event.objects.filter(pk=body['id']).update(
                    status=body['action'])
                return JsonResponse({"success": True}, status=200)
        except Exception:
            return JsonResponse({"success": False}, status=400)
    return JsonResponse({"success": False}, status=400)


def add_new(request,date_string=None):
    categories = Category.objects.all()

    if request.method == 'POST':
        event_form = AddEventForm(request.POST or None)

        if event_form.is_valid():
            event = event_form.save(commit=False)
            event.save()

            return redirect('event_day', date_string=event.dt)
        else:
            return HttpResponse(event_form.errors)
    else:
        empty_event=Event(dt=date_string)
        event_form = AddEventForm(instance=empty_event)
    return render(request, 'calendar/new_event.html', {'event_form': event_form, 'categories': categories})

def add_new_category(request):
    if request.method == 'POST':
        category_form = AddCategoryForm(request.POST or None)

        if category_form.is_valid():
            category = category_form.save(commit=False)
            category.save()

            return redirect('new_event')
        else:
            return HttpResponse(category_form.errors)
    else:
        category_form = AddCategoryForm()
    return render(request, 'calendar/new_category.html', {'category_form': category_form})


def add_new_habbit(request):
    categories = Category.objects.all()
    if request.method == 'POST':
        form_data = request.POST
        category = get_object_or_404(categories, name=form_data['category'])
        new_habit = Habit(
            category=category,
            name=form_data['name'],
        )
        new_habit.save()
        all_dates=list(form_data.values())[4:]
        all_dates=[(all_dates[i],all_dates[i+1]) for i in range(0,len(all_dates),2)]
        for k,v in all_dates:
            if k and v:
                new_event = Event(
                    category=category,
                    name=form_data['event_name'],
                    status='ACTIVE',
                    dt=k,
                    tm=v
                )
                new_event.save()
                dt = datetime.strptime(k, "%Y-%m-%d").date()
                time_delta = timedelta(days=7)
                year_end = date(year=my_year, month=12, day=31)
                dt += time_delta
                all_events = []
                all_events.append(new_event)
                while dt <= year_end:
                    add_event = Event(
                        category=category,
                        name=form_data['event_name'],
                        dt=dt.strftime("%Y-%m-%d"),
                        tm=v
                    )
                    add_event.save()
                    all_events.append(add_event)
                    dt += time_delta

                for event in all_events:
                    habit_event = Habits_Events(
                        habit_id=new_habit,
                        event_id=event

                    )
                    habit_event.save()
            else:
                break
        return redirect('calendar')
    else:
        return render(request, 'calendar/new_habit.html', {'categories': categories})


def habits(request):
    habits = Habit.objects.all()
    context = {
        'habits': habits
    }
    return render(request, 'calendar/habits_list.html', context=context)


def habit_card(request, habit_id):
    habit=get_object_or_404(Habit, id=habit_id)
    if request.method == 'POST':
        habit_form = EditCategoryForm(request.POST, instance=habit)

        if habit_form.is_valid():
            upd_habit = habit_form.save(commit=False)
            upd_habit.save()

            return redirect('habit',habit.id)
        else:
            return HttpResponse(habit_form.errors)
    else:
        habit_form = EditCategoryForm(instance=habit)
    return render(request, 'calendar/habit_card.html', {'habit_form': habit_form,'habit':habit})


def delete_habit(request, habit_id):
    habits_event = Habits_Events.objects.filter(habit_id=habit_id)
    for habit_event in habits_event:
        event = get_object_or_404(Event, id=habit_event.event_id.id)
        event.delete()
    habit = get_object_or_404(Habit, id=habits_event[0].habit_id.id)
    habit.delete()
    return redirect('habits')

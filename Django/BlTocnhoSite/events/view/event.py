from django.shortcuts import render
from django.http import HttpResponse
from events.forms import AddEventForm
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from events.models import Event, Category
from django.http import HttpResponse, JsonResponse
from datetime import date, datetime, timedelta


def add_new(request, date_string=None):
    categories = Category.objects.all()

    if request.method == 'POST':
        event_form = AddEventForm(request.POST or None)

        if event_form.is_valid():
            event = event_form.save(commit=False)
            event.save()
            if event.dt == date(year=1999, month=1, day=1):
                return redirect('home')
            return redirect('event_day', date_string=event.dt)
        else:
            return HttpResponse(event_form.errors)
    else:
        if not date_string:
            date_string = '1999-01-01'
        empty_event = Event(dt=date_string)
        event_form = AddEventForm(instance=empty_event)
    return render(request, 'calendar/event/new_event.html', {'event_form': event_form, 'categories': categories})


def event(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    if request.method == 'POST':
        event_form = AddEventForm(request.POST, instance=event)

        if event_form.is_valid():
            updt_event = event_form.save(commit=False)
            updt_event.save()

            return redirect('event', event.id)
        else:
            return HttpResponse(event_form.errors)
    else:
        event_form = AddEventForm(instance=event)
    return render(request, 'calendar/event/event_card.html', {'event_form': event_form, 'event': event})


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

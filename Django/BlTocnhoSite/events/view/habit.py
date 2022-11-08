from calendar import month
from datetime import date, datetime, timedelta
from django.shortcuts import render
from django.http import HttpResponse
from events.forms import EditCategoryForm,Habits_EventsForm
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from events.models import Event, Category, Habit, Habits_Events
from dateutil.relativedelta import relativedelta
today = date.today()
my_year = today.year
my_month = today.month
my_day = today.day


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
        period = form_data['period']
        all_dates = list(form_data.values())[5:]
        all_dates = [(all_dates[i], all_dates[i+1],all_dates[i+2],all_dates[i+3])
                     for i in range(0, len(all_dates), 4)]
        for k, v , v_end,v_road in all_dates:
            if k and v:
                new_event = Event(
                    category=category,
                    name=form_data['event_name'],
                    status='ACTIVE',
                    dt=k,
                    tm_start=v,
                    tm_end=v_end,
                    tm_road=v_road
                )
                new_event.save()
                dt = datetime.strptime(k, "%Y-%m-%d").date()
                if period == "EveryWeek":
                    time_delta = timedelta(days=7)
                    year_end = date(year=my_year, month=12, day=31)
                elif period == "EveryDay":
                    time_delta = timedelta(days=1)
                    year_end = date(year=my_year, month=12, day=31)
                elif period == "EveryMonth":
                    time_delta = relativedelta(days=30)
                    year_end = date(year=my_year, month=12, day=31)
                elif period == "EveryYear":
                    time_delta = relativedelta(days=365)
                    year_end = date(year=my_year+10, month=12, day=31)
                dt += time_delta
                all_events = []
                all_events.append(new_event)
                while dt <= year_end:
                    add_event = Event(
                        category=category,
                        name=form_data['event_name'],
                        dt=dt.strftime("%Y-%m-%d"),
                        tm_start=v,
                        tm_end=v_end,
                        tm_road=v_road
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
        return render(request, 'calendar/habit/new_habit.html', {'categories': categories})


def habits(request):
    habits = Habit.objects.all()
    context = {
        'habits': habits
    }
    return render(request, 'calendar/habit/habits_list.html', context=context)


# def habit_card(request, habit_id):
#     habit = get_object_or_404(Habit, id=habit_id)
#     if request.method == 'POST':
#         habit_form = EditCategoryForm(request.POST, instance=habit)

#         if habit_form.is_valid():
#             upd_habit = habit_form.save(commit=False)
#             upd_habit.save()

#             return redirect('habit', habit.id)
#         else:
#             return HttpResponse(habit_form.errors)
#     else:
#         habit_form = EditCategoryForm(instance=habit)
#     return render(request, 'calendar/habit/habit_card.html', {'habit_form': habit_form, 'habit': habit})

def habit_card(request, habit_id):
    habit = get_object_or_404(Habit, id=habit_id)
    if request.method == 'POST':
        habit_form = Habits_EventsForm(request.POST, instance=habit)

        if habit_form.is_valid():
            upd_habit = habit_form.save(commit=False)
            upd_habit.save()

            return redirect('habit', habit.id)
        else:
            return HttpResponse(habit_form.errors)
    else:
        habit_form = Habits_EventsForm(instance=habit)
    return render(request, 'calendar/habit/habit_card.html', {'habit_form': habit_form, 'habit': habit})


def delete_habit(request, habit_id):
    habits_event = Habits_Events.objects.filter(habit_id=habit_id)
    for habit_event in habits_event:
        event = get_object_or_404(Event, id=habit_event.event_id.id)
        event.delete()
    habit = get_object_or_404(Habit, id=habits_event[0].habit_id.id)
    habit.delete()
    return redirect('habits')

from datetime import date, timedelta
from django.shortcuts import render
from django.http import HttpResponse

today=date.today()
my_year=today.year
my_month=today.month


def calendar(request,year:int=None,month:int=None):
    if not year:
        year=my_year
    if not month:
        month=my_month
    print(year)
    print(month)
    month_html=calendar_builder(year,month)
    context={
        'month_list': month_html,
        'year':year,
        'month':month,
        'prev_month':month-1,
        'next_month':month+1
    }
    return render(request, 'calendar/calendar.html',context=context)



def event(request,event_id):
    print(event_id)
    return render(request, 'calendar/event_list.html')


def add_event(request):
    req=request
    print('hiii')



def calendar_builder(year:int=None,month:int=None)->dict:
    print(year)
    print(month)
    start_day=date(year,month,1)
    end_day=date(year,month+1,1) - timedelta(days=1)
    start_day=start_day-timedelta(days=start_day.weekday())
    month=[]
    index=1
    while start_day<=end_day:
        week=['','','','','','','']
        for day_index in range(7):
            week[start_day.weekday()]=start_day
            if start_day.weekday()==6:
                break
            else:
                start_day+=timedelta(days=1)
                continue
        month.append(week)
        start_day+=timedelta(days=1)
        index+=1
    return month
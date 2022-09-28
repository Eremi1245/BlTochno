from datetime import date, time
from django import template
from django.template.defaulttags import register
from events.utils import status_choise_for_tag_filter
register = template.Library()

@register.filter
def rng(obj:object):
    print('dsads')
    return range(len(obj))

@register.filter
def index(indexable, i):
    return indexable[i]
    
@register.filter
def month_to_string(weekday:int):
    if weekday==1:
        weekday='Января'
    elif weekday==2:
        weekday='Февраля'
    elif weekday==3:
        weekday='Марта'
    elif weekday==4:
        weekday='Апреля'
    elif weekday==5:
        weekday='Мая'
    elif weekday==6:
        weekday='Июня'
    elif weekday==7:
        weekday='Июля'
    elif weekday==8:
        weekday='Августа'
    elif weekday==9:
        weekday='Сентября'
    elif weekday==10:
        weekday='Октября'
    elif weekday==11:
        weekday='Ноября'
    elif weekday==12:
        weekday='Декабря'
    return weekday

@register.filter
def good_dt(bad_tm:time):
    return bad_tm.strftime('%H: %M')

@register.filter
def dt_handler(dt:date)->int:
    return f'{dt.day} {month_to_string(dt.month)}'

@register.filter
def status_handler(status:str)->str:
    return status_choise_for_tag_filter[status]

@register.filter
def in_processig_handler(status:str,right_status:str)->bool:
    if status==right_status:
        return True
    else:
        return False
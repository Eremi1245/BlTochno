from datetime import date
from django import template
from django.template.defaulttags import register

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
def dt_handler(dt:date)->int:
    return f'{dt.day} {month_to_string(dt.month)}'
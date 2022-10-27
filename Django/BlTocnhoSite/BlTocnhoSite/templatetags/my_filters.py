from datetime import date, datetime, time,timedelta
from django import template
from django.template.defaulttags import register
from events.models import Event
from events.utils import status_choise_for_tag_filter
import random
register = template.Library()


@register.filter
def rng(obj: object):
    print('dsads')
    return range(len(obj))


@register.filter
def index(indexable, i):
    return indexable[i]


@register.filter
def month_to_string(weekday: int):
    if weekday == 1:
        weekday = 'Января'
    elif weekday == 2:
        weekday = 'Февраля'
    elif weekday == 3:
        weekday = 'Марта'
    elif weekday == 4:
        weekday = 'Апреля'
    elif weekday == 5:
        weekday = 'Мая'
    elif weekday == 6:
        weekday = 'Июня'
    elif weekday == 7:
        weekday = 'Июля'
    elif weekday == 8:
        weekday = 'Августа'
    elif weekday == 9:
        weekday = 'Сентября'
    elif weekday == 10:
        weekday = 'Октября'
    elif weekday == 11:
        weekday = 'Ноября'
    elif weekday == 12:
        weekday = 'Декабря'
    return weekday


@register.filter
def good_dt(bad_tm: time):
    return bad_tm.strftime('%H: %M')


@register.filter
def dt_handler(dt: date) -> int:
    return f'{dt.day} {month_to_string(dt.month)}'


@register.filter
def dt_handler_for_title(dt: str) -> str:
    dt_format = datetime.strptime(dt, '%Y-%m-%d')
    weekday = weekday_to_string(dt_format.weekday())
    return f'{weekday} {dt_format.day} {month_to_string(dt_format.month)}'


def weekday_to_string(weekday: int):
    if weekday == 0:
        return 'Понедельник'
    elif weekday == 1:
        return 'Вторник'
    elif weekday == 2:
        return 'Среда'
    elif weekday == 3:
        return 'Четверг'
    elif weekday == 4:
        return 'Пятница'
    elif weekday == 5:
        return 'Суббота'
    elif weekday == 6:
        return 'Воскресенье'


@register.filter
def status_handler(status: str) -> str:
    return status_choise_for_tag_filter[status]


@register.filter
def in_processig_handler(status: str, right_status: str) -> bool:
    if status == right_status:
        return True
    else:
        return False


@register.filter
def data_checker(dt: date) -> bool:
    today = datetime.today().date()
    if today > dt:
        return True
    else:
        return False


@register.filter
def get_style_for_timeline(event: Event,div_flag:bool) -> str:
    dt_start=datetime(year=event.dt.year,month=event.dt.month,day=event.dt.day,hour=event.tm_start.hour,minute=event.tm_start.minute)
    dt_end=datetime(year=event.dt.year,month=event.dt.month,day=event.dt.day,hour=event.tm_end.hour,minute=event.tm_end.minute)
    event_longer=dt_end-dt_start
    one_hour_seconds=3600
    element_width=(event_longer.seconds*100)/86400
    margin_element=((one_hour_seconds*(dt_start.hour+dt_start.minute/100))*100)/86400
    color=random_color()
    if div_flag:
        return f"width:{element_width}%;margin-left:{margin_element}%;background:{color};height: 15px;"
    else:
        return f"width:{element_width}%;margin-left:{margin_element}%;"

@register.filter
def get_style_current_timeline():
    now=datetime.now()
    one_hour_seconds=3600
    margin_element=(one_hour_seconds*(now.hour+now.minute/100+now.second/100)*100)/86400
    return f"margin-left:{margin_element}%;"

def random_color()->str:
    r = lambda: random.randint(0,255)
    return '#%02X%02X%02X' % (r(),r(),r())
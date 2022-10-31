from time import sleep
import requests
from datetime import datetime, timedelta


handicap_for_otification = 10
api_url = 'http://127.0.0.1:8000/api/events/'


def parse_notification_time(event) -> str:
    tm_start = datetime.strptime(
        event['dt']+event['tm_start'], "%Y-%m-%d%H:%M:%S")
    tm_road = datetime.strptime(event['tm_road'], "%H:%M:%S")
    tm_road = timedelta(hours=tm_road.hour, minutes=tm_road.minute +
                        handicap_for_otification, seconds=tm_road.second)
    notification_time = tm_start-tm_road
    notification_time = notification_time.strftime('%H:%M')
    return notification_time


def text_notification_build(event)->str:
    tm_start = event['tm_start'][:-3]
    tm_end = event['tm_end'][:-3]
    tm_road = event['tm_road'][:-3]
    name = event['name'].upper()
    desc = event['desc']
    text_notification = f'{name}:\nСегодня с {tm_start} по {tm_end}\nДорога {tm_road}:\n"{desc}":\n'
    return text_notification


def notification():
    today_events_dict = {
        'td_today': datetime.today().strftime("%Y-%m-%d"),
        'len_events': 0,
        'event_list': dict()
    }
    while True:
        today = datetime.today().strftime("%Y-%m-%d")
        if today_events_dict['td_today'] == today:
            url = api_url+today
            today_events = requests.get(url=url).json()
            if today_events_dict['len_events'] == len(today_events):
                pass
            else:
                today_events_dict['len_events'] = len(today_events)
                today_events_dict['event_list'] = dict()
                for event in today_events:
                    notification_time = parse_notification_time(event)
                    today_events_dict['event_list'][notification_time] = event
            time_now = datetime.today().strftime("%H:%M")
            text_notification_dict = today_events_dict['event_list']
            try:
                event = text_notification_dict[time_now]
                text_notification = text_notification_build(event)
                # send notification
                requests.get(
                    url='https://api.telegram.org/bot5446878932:AAE_wmAPKXEXlsTJHc1b49We7y7SX_Ns4Xk/sendMessage',
                    data={'chat_id': '294350087',
                          'text': text_notification,
                          'parse_mode': 'HTML'})
            except KeyError:
                pass
            except Exception as er:
                requests.get(
                    url='https://api.telegram.org/bot5446878932:AAE_wmAPKXEXlsTJHc1b49We7y7SX_Ns4Xk/sendMessage',
                    data={'chat_id': '294350087',
                          'text': er,
                          'parse_mode': 'HTML'})
            sleep(60)
        else:
            today_events_dict.clear()
            today_events_dict['td_today'] = datetime.today().strftime(
                "%Y-%m-%d")
            today_events_dict['len_events'] = 0
            today_events_dict['event_list'] = dict()


notification()

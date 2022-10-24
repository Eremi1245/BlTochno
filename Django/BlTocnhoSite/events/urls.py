from django.urls import path
from events.view.calendar import calendar
from events.view.event import add_new,event,event_action,planning_events,passed_events,succes_events,no_succes_events
from events.view.habit import add_new_habbit,habit_card,delete_habit,habits
from events.view.day import events_day
from events.view.category import add_new_category
urlpatterns = [
    path('', calendar,name='calendar'),
    path('calendar/<int:year>/<int:month>', calendar,name='calendar'),
    path('day/<str:date_string>',events_day,name='event_day'),
    path('event/<int:event_id>/',event,name='event'),
    path('ajax/contact/', event_action, name ='event_action'),
    path('event/add_new/', add_new, name ='new_event'),
    path('event/add_new/<str:date_string>', add_new, name ='new_event'),
    path('category/add_new/', add_new_category, name ='new_category'),
    path('habit/add_new/', add_new_habbit, name ='new_habit'),
    path('habits/', habits, name ='habits'),
    path('habits/<int:habit_id>/',habit_card,name ='habit'),
    path('habits/delete/<int:habit_id>/',delete_habit,name ='delete_habit'),
    path('event/planning_events', planning_events, name ='planning_events'),
    path('event/passed_events', passed_events, name ='passed_events'),
    path('event/succes_events', succes_events, name ='succes_events'),
    path('event/no_succes_events', no_succes_events, name ='no_succes_events'),
    # path('event/add_event',add_event)
]

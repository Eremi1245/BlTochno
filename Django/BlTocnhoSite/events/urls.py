from django.urls import path

from events.views import calendar,event,add_event,events_day
urlpatterns = [
    path('', calendar,name='calendar'),
    path('<int:year>/<int:month>', calendar),
    path('day/<str:date_string>',events_day,name='event_day'),
    path('event/<int:event_id>/',event),
    path('event/add_event',add_event)
]

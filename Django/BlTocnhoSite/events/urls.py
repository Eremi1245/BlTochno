from django.urls import path

from events.views import calendar,event,events_day,event_action,add_new,add_new_category,add_new_habbit,habits
urlpatterns = [
    path('', calendar,name='calendar'),
    path('<int:year>/<int:month>', calendar),
    path('day/<str:date_string>',events_day,name='event_day'),
    path('event/<int:event_id>/',event),
    path('ajax/contact/', event_action, name ='event_action'),
    path('event/add_new/', add_new, name ='new_event'),
    path('category/add_new/', add_new_category, name ='new_category'),
    path('habit/add_new/', add_new_habbit, name ='new_habit'),
    path('habits/', habits, name ='habits'),
    # path('event/add_event',add_event)
]

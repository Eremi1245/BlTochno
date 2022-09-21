from django.urls import path

from events.views import calendar,event,add_event
urlpatterns = [
    path('', calendar),
    path('<int:year>/<int:month>', calendar),
    path('event/<int:event_id>/',event),
    path('event/add_event',add_event)
]

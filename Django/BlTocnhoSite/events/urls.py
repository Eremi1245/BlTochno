from django.urls import path

from events.views import calendar,event
urlpatterns = [
    path('', calendar),
    path('event/<int:event_id>/',event)
]


from datetime import date
from rest_framework import serializers, viewsets
from events.models import Event


class EventSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Event
        fields = ['name', 'status','category','desc','dt','tm']
        lookup_field='category'

class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all().filter(dt=date.today()).order_by('tm')
    serializer_class = EventSerializer
    lookup_field='category'
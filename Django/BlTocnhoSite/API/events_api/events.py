
from datetime import date
from rest_framework import serializers, viewsets
from events.models import Event
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status

class EventSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Event
        fields = ['name', 'status','category','desc','dt','tm']
        lookup_field='category'

class EventViewSet(viewsets.ModelViewSet):

    queryset = Event.objects.all()
    serializer_class = EventSerializer
    lookup_field='category'
    
    @action(detail=True,methods=['get'])
    def get_all(self,requets):
        print(requets)
        queryset = self.queryset.filter(dt=date.today()).order_by('tm')
        return Response(self.serializer_class(queryset,many=True).data,status=status.HTTP_200_OK)




# def delete_event(request,id):
#     queryset = Event.objects.filter(id=id).delete()
#     print(queryset)
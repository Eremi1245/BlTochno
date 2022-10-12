
from datetime import date
from rest_framework import serializers, viewsets
from events.models import Event
from rest_framework.decorators import action,api_view
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from events.utils import status_choise
class EventSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = Event
        fields = ['id','category','name', 'dt', 'tm','status','desc']
        lookup_field='category'

class EventViewSet(viewsets.ViewSet):

    def list(self, request):
        queryset = Event.objects.all()
        serializer = EventSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        pass

    def retrieve(self, request, pk=None):
        queryset = Event.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = EventSerializer(user)
        return Response(serializer.data)

    def update(self, request, pk=None,updt_status=None):
        try:
            Event.objects.filter(pk=id).update(status=updt_status)
            return Response(status.HTTP_200_OK)
        except Exception as er:
            print(er)
            return Response(status.HTTP_400_BAD_REQUEST)

    def partial_update(self, request, pk=None):
        pass

    def destroy(self, request, pk=None):
        queryset = Event.objects.all()
        evet_delete=queryset.filter(pk=pk).delete()
        print(evet_delete)
        return Response(status.HTTP_200_OK)

from dataclasses import field
from datetime import date
from django.urls import path, include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from events.models import Category, Event

# Serializers define the API representation.
class EventSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Event
        fields = ['name', 'status','category','desc','dt','tm']
        lookup_field = 'category'

class CategorySerializer(serializers.HyperlinkedModelSerializer):
    category = serializers.HyperlinkedRelatedField(
        view_name='category-detail',
        read_only=True,
        lookup_field='category'
    )
    class Meta:
        model = Category
        fields=['name','category']


# ViewSets define the view behavior.
class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all().filter(dt=date.today())
    serializer_class = EventSerializer
    lookup_field='category'

class EventViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all().select_related('name')
    serializer_class = CategorySerializer
    lookup_field='name'

# class CategoryViewSet(viewsets.ModelViewSet):
#     queryset = Category.objects.all()
#     serializer_class = SpeakerSerializer
#     lookup_field = "user"


# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'events', EventViewSet)


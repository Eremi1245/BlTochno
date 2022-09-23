from rest_framework import routers, serializers, viewsets
from API.events_api.events import EventViewSet
from API.events_api.category import CategoryViewSet
from django.urls import path,include
from rest_framework.routers import DefaultRouter



router = DefaultRouter()
router.register(r'events', EventViewSet, basename='event')
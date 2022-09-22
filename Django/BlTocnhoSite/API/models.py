from rest_framework import routers, serializers, viewsets
from API.events_api.events import EventViewSet
from API.events_api.category import CategoryViewSet


# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'events', EventViewSet)
router.register(r'category', CategoryViewSet)




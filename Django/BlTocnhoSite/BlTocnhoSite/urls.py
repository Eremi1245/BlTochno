
from django.contrib import admin
from django.urls import path,include
from .views import index
from API.urls import router
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('calendar/',include('events.urls')),
    path('',index,name='home'),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include(router.urls)),
]

urlpatterns+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
"""events_project/urls.py"""

from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from events.views import EventViewSet, EventRegistrationViewSet
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularSwaggerView,
)


router = DefaultRouter()
router.register(r'events', EventViewSet)
router.register(r'event-register', EventRegistrationViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('api/health-check/', userManager.health_check, name='health-check'),
    path('api/schema/', SpectacularAPIView.as_view(), name='api-schema'),
    path('api/docs/', SpectacularSwaggerView.as_view(
        url_name='api-schema'
        ), name='api-docs'),
    path('api/', include(router.urls)),
    path('api/user/', include('userManager.urls')),
]

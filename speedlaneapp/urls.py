from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (LaneViewSet,TurnStyleViewSet,SystemConfigViewSet,AccessLogViewSet,)

router = DefaultRouter()

router.register(r"lanes", LaneViewSet, basename="lane")
router.register(r"turnstyles", TurnStyleViewSet, basename="turnstyle")
router.register(r"system-config", SystemConfigViewSet, basename="system-config")
router.register(r"access-logs", AccessLogViewSet, basename="access-log")

urlpatterns = router.urls

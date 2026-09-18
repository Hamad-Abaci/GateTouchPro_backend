from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (LaneViewSet,TurnStyleViewSet,SystemConfigViewSet,AccessLogViewSet, LaneGroupViewSet)

router = DefaultRouter()

router.register(r"lanes", LaneViewSet, basename="lane")
router.register(r"turnstyles", TurnStyleViewSet, basename="turnstyle")
router.register(r"system-config", SystemConfigViewSet, basename="system-config")
router.register(r"access-logs", AccessLogViewSet, basename="access-log")
router.register(r"lane-groups", LaneGroupViewSet, basename="lane-group")

urlpatterns = router.urls

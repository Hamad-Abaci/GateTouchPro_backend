from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import (Lane, TurnStyle, SystemConfig, AccessLog)

from .serializers import (
    LaneSerializer,
    TurnStyleSerializer,
    SystemConfigSerializer,
    AccessLogSerializer,
)


class LaneViewSet(viewsets.ModelViewSet):

    queryset = Lane.objects.prefetch_related("turnstyles").all()
    serializer_class = LaneSerializer

    @action(detail=True, methods=["patch"])
    def trigger(self, request, pk=None):

        lane = self.get_object()

        remarks = request.data.get("remarks")

        AccessLog.objects.create(
            lane=lane,
            user=request.data.get("user"),
            remarks=remarks
        )
        return Response({"message": "Lane triggered successfully","lane_id": lane.id},status=status.HTTP_200_OK)


class TurnStyleViewSet(viewsets.ModelViewSet):

    queryset = TurnStyle.objects.all()
    serializer_class = TurnStyleSerializer


class SystemConfigViewSet(viewsets.ModelViewSet):

    queryset = SystemConfig.objects.all()
    serializer_class = SystemConfigSerializer


class AccessLogViewSet(viewsets.ModelViewSet):

    queryset = AccessLog.objects.select_related("lane").order_by("-triggered_at")
    serializer_class = AccessLogSerializer
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .lane_trrigger import set_status
from .models import (Lane, TurnStyle, SystemConfig, AccessLog, LaneGroup)

from .serializers import (
    LaneSerializer,
    TurnStyleSerializer,
    SystemConfigSerializer,
    AccessLogSerializer,
    LaneGroupSerializer
)


class LaneGroupViewSet(viewsets.ModelViewSet):

    queryset = LaneGroup.objects.prefetch_related("lanes").all()
    serializer_class = LaneGroupSerializer

class LaneViewSet(viewsets.ModelViewSet):

    queryset = Lane.objects.prefetch_related("turnstyles").all()
    serializer_class = LaneSerializer

    @action(detail=True, methods=["patch"] ,   url_path=r"trigger/(?P<direction>entry|exit)")
    def trigger(self, request, direction, pk=None):

        lane = self.get_object()

        if direction not in ["entry", "exit"]:
            return Response(
                {"error": "Invalid direction"},
                status=status.HTTP_400_BAD_REQUEST
            )

        turnstyles = lane.turnstyles.all()

        for turnstyle in turnstyles:

            if direction == "entry":
                pin = turnstyle.entry_pin
            else:
                pin = turnstyle.exit_pin

            set_status(pin)

        remarks = request.data.get("remarks")

        AccessLog.objects.create(
            lane=lane,
            user=request.data.get("user"),
            remarks=remarks
        )

        return Response(
            {
                "message": "Lane triggered successfully",
                "lane_id": lane.id,
                "direction": direction
            },
            status=status.HTTP_200_OK
        )


class TurnStyleViewSet(viewsets.ModelViewSet):

    queryset = TurnStyle.objects.all()
    serializer_class = TurnStyleSerializer


class SystemConfigViewSet(viewsets.ModelViewSet):

    queryset = SystemConfig.objects.all()
    serializer_class = SystemConfigSerializer


class AccessLogViewSet(viewsets.ModelViewSet):

    queryset = AccessLog.objects.select_related("lane").order_by("-triggered_at")
    serializer_class = AccessLogSerializer
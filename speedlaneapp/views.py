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

    queryset = LaneGroup.objects.prefetch_related(
        "lanes__turnstyles"
    ).all()

    serializer_class = LaneGroupSerializer

    @action(
        detail=True,
        methods=["patch"],
        url_path=r"trigger/(?P<direction>entry|exit)"
    )
    def trigger(self, request, direction, pk=None):

        lane_group = self.get_object()
        if direction not in ["entry", "exit"]:
          direction = "entry"

        lanes = lane_group.lanes.all()

        pins = set()

        for lane in lanes:

            if direction == "entry":
                pins.add(lane.entry_pin)
            else:
                pins.add(lane.exit_pin)
        config = SystemConfig.objects.get(pk=1)
        delay=config.trigger_delay
        for pin in pins:
            set_status(pin, delay)
            print(f"Triggering GPIO pin: {pin} for {delay} ms")

        for lane in lanes:
            AccessLog.objects.create(
                lane=lane,
                user=request.data.get("user"),
                remarks=request.data.get("remarks")
            )

        return Response(
            {
                "message": "Lane group trigger started successfully",
                "lane_group_id": lane_group.id,
                "direction": direction
            },
            status=status.HTTP_200_OK
        )


 


class LaneViewSet(viewsets.ModelViewSet):

    queryset = Lane.objects.prefetch_related("turnstyles").all()
    serializer_class = LaneSerializer

    @action(detail=True, methods=["patch"] ,   url_path=r"trigger/(?P<direction>entry|exit)")
    def trigger(self, request, direction, pk=None):

        lane = self.get_object()

        if direction not in ["entry", "exit"]:
          direction = "entry" 
        config = SystemConfig.objects.get(pk=1)
        delay=config.trigger_delay

        if direction == "entry":
            pin = lane.entry_pin
        else:
            pin = lane.exit_pin

        set_status(pin,delay)
        print(f"Triggering GPIO pin: {pin} for {delay} ms")

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
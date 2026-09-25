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
        url_path="trigger/emergency"
    )
    def trigger_emergency(self, request, pk=None):

        lane_group = self.get_object()

        config = SystemConfig.get_config()
        delay = config.trigger_delay

        pin = lane_group.emergency_pin

        set_status(pin, delay)

        print(
            f"Triggering emergency GPIO pin: "
            f"{pin} for {delay} ms"
        )
        AccessLog.objects.create(
        lane_group=lane_group,
        user=request.data.get("user"),
        type="emergency",
        remarks=request.data.get("remarks")
    )

        return Response(
            {
                "message": "Emergency trigger started successfully",
                "lane_group_id": lane_group.id,
                "pin": pin
            },
            status=status.HTTP_200_OK
        )


    @action(
        detail=True,
        methods=["patch"],
        url_path="trigger/fire"
    )
    def trigger_fire(self, request, pk=None):

        lane_group = self.get_object()

        config = SystemConfig.get_config()
        delay = config.trigger_delay

        pin = lane_group.fire_pin

        set_status(pin, delay)

        print(
            f"Triggering fire GPIO pin: "
            f"{pin} for {delay} ms"
        )
        AccessLog.objects.create(
        lane_group=lane_group,
        user=request.data.get("user"),
        type="fire",
        remarks=request.data.get("remarks")
    )

        return Response(
            {
                "message": "Fire trigger started successfully",
                "lane_group_id": lane_group.id,
                "pin": pin
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
        lane_delay =lane.delay
        if lane_delay:
            delay=lane_delay
        else:
            config = SystemConfig.get_config()
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
            type="normal",
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

    queryset = AccessLog.objects.select_related("lane","lane_group").order_by("-triggered_at")
    serializer_class = AccessLogSerializer
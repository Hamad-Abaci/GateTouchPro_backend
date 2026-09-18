from rest_framework import serializers

from .models import (
    Lane,
    LaneGroup,
    TurnStyle,
    SystemConfig,
    AccessLog
)


class TurnStyleSerializer(serializers.ModelSerializer):
    class Meta:
        model = TurnStyle
        fields = "__all__"


class LaneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lane
        fields = "__all__"


class LaneGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = LaneGroup
        fields = "__all__"


class SystemConfigSerializer(serializers.ModelSerializer):
    class Meta:
        model = SystemConfig
        fields = "__all__"


class AccessLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccessLog
        fields = "__all__"
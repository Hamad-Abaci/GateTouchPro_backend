from rest_framework import serializers

from .models import (
    Lane,
    LaneGroup,
    TurnStyle,
    SystemConfig,
    AccessLog
)


class TurnStyleSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)

    class Meta:
        model = TurnStyle
        fields = "__all__"

class LaneSerializer(serializers.ModelSerializer):
    turnstyles = TurnStyleSerializer(many=True)

    class Meta:
        model = Lane
        fields = [
            "id",
            "name",
            "lane_group",
            "turnstyles",
            "width",
            "created_by",
            "created_at",
            "updated_by",
            "updated_at",
            "deleted_by",
            "deleted_at",
        ]

    def create(self, validated_data):
        turnstyles_data = validated_data.pop("turnstyles", [])

        lane = Lane.objects.create(**validated_data)

        for turnstyle_data in turnstyles_data:
            turnstyle = TurnStyle.objects.create(**turnstyle_data)
            lane.turnstyles.add(turnstyle)

        return lane

    def update(self, instance, validated_data):
        turnstyles_data = validated_data.pop("turnstyles", None)

        # Update Lane fields
        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        instance.save()

        if turnstyles_data is not None:
            instance.turnstyles.clear()

            for turnstyle_data in turnstyles_data:
                turnstyle_id = turnstyle_data.pop("id", None)

                if turnstyle_id:
                    turnstyle = TurnStyle.objects.get(id=turnstyle_id)

                    for attr, value in turnstyle_data.items():
                        setattr(turnstyle, attr, value)

                    turnstyle.save()
                else:
                    turnstyle = TurnStyle.objects.create(**turnstyle_data)

                instance.turnstyles.add(turnstyle)

        return instance
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
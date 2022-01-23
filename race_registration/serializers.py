from rest_framework import serializers

from . import models


class resultSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.result
        fields = [
            "created",
            "last_updated",
            "start_time",
            "finish_time",
        ]

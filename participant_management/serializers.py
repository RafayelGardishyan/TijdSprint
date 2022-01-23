from rest_framework import serializers

from . import models


class boat_typeSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.boat_type
        fields = [
            "correction",
            "code",
            "created",
            "last_updated",
        ]

class raceSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.race
        fields = [
            "end_date",
            "last_updated",
            "description",
            "start_date",
            "name",
            "created",
        ]

class crewSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.crew
        fields = [
            "last_updated",
            "name",
            "created",
        ]

class rowerSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.rower
        fields = [
            "gender",
            "slug",
            "full_name",
            "created",
            "last_updated",
            "date_of_birth",
        ]

class boatSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.boat
        fields = [
            "last_updated",
            "created",
            "name",
            "slug",
        ]

class heatSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.heat
        fields = [
            "name",
            "last_updated",
            "created",
            "distance",
            "start_time",
        ]

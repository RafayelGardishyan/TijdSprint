from rest_framework import viewsets, permissions

from . import serializers
from . import models


class boat_typeViewSet(viewsets.ModelViewSet):
    """ViewSet for the boat_type class"""

    queryset = models.boat_type.objects.all()
    serializer_class = serializers.boat_typeSerializer
    permission_classes = [permissions.IsAuthenticated]


class raceViewSet(viewsets.ModelViewSet):
    """ViewSet for the race class"""

    queryset = models.race.objects.all()
    serializer_class = serializers.raceSerializer
    permission_classes = [permissions.IsAuthenticated]


class crewViewSet(viewsets.ModelViewSet):
    """ViewSet for the crew class"""

    queryset = models.crew.objects.all()
    serializer_class = serializers.crewSerializer
    permission_classes = [permissions.IsAuthenticated]


class rowerViewSet(viewsets.ModelViewSet):
    """ViewSet for the rower class"""

    queryset = models.rower.objects.all()
    serializer_class = serializers.rowerSerializer
    permission_classes = [permissions.IsAuthenticated]


class boatViewSet(viewsets.ModelViewSet):
    """ViewSet for the boat class"""

    queryset = models.boat.objects.all()
    serializer_class = serializers.boatSerializer
    permission_classes = [permissions.IsAuthenticated]


class heatViewSet(viewsets.ModelViewSet):
    """ViewSet for the heat class"""

    queryset = models.heat.objects.all()
    serializer_class = serializers.heatSerializer
    permission_classes = [permissions.IsAuthenticated]

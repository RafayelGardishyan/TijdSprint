from rest_framework import viewsets, permissions

from . import serializers
from . import models


class resultViewSet(viewsets.ModelViewSet):
    """ViewSet for the result class"""

    queryset = models.result.objects.all()
    serializer_class = serializers.resultSerializer
    permission_classes = [permissions.IsAuthenticated]

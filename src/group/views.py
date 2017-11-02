from rest_framework import viewsets

from common import mixins
from . import models
from . import serializers

class LenderGroupViewSet(mixins.RelativeURLFieldMixin, viewsets.ModelViewSet):
    queryset = models.LenderGroup.objects.all()
    serializer_class = serializers.LenderGroupSerializer

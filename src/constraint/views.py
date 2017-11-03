from rest_framework import viewsets

from common import mixins
from . import models
from . import serializers


class ConstraintViewSet(mixins.RelativeURLFieldMixin, viewsets.ModelViewSet):
    queryset = models.Constraint.objects.all()
    serializer_class = serializers.ConstraintSerializer

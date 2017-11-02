from rest_framework import viewsets

from common import mixins
from . import models
from . import serializers


class LoanViewSet(mixins.RelativeURLFieldMixin, viewsets.ModelViewSet):
    queryset = models.Loan.objects.all()
    serializer_class = serializers.LoanSerializer


class ResourceViewSet(mixins.RelativeURLFieldMixin, viewsets.ModelViewSet):
    queryset = models.Resource.objects.all()
    serializer_class = serializers.ResourceSerializer


class ResourceTypeViewSet(mixins.RelativeURLFieldMixin, viewsets.ModelViewSet):
    queryset = models.ResourceType.objects.all()
    serializer_class = serializers.ResourceTypeSerializer

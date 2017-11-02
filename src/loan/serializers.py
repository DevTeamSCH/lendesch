from rest_framework import serializers

from . import models


class LoanSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        fields = serializers.ALL_FIELDS
        model = models.Loan


class ResourceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        fields = serializers.ALL_FIELDS
        model = models.Resource


class ResourceTypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        fields = serializers.ALL_FIELDS
        model = models.ResourceType

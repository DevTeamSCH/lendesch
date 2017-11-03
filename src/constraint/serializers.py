from rest_framework import serializers

from . import models


class ConstraintSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        fields = serializers.ALL_FIELDS
        model = models.Constraint

from django.contrib.auth.models import User
from rest_framework import serializers

from . import models


class LenderGroupSerializer(serializers.HyperlinkedModelSerializer):
    administrators = serializers.HyperlinkedRelatedField(
        many=True,
        view_name='user-detail',
        queryset=User.objects.all()
    )
    class Meta:
        fields = ('url', 'name', 'administrators')
        model = models.LenderGroup

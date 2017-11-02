from django.contrib.auth.models import User
from rest_framework import viewsets

from common import mixins
from . import serializers


class AccountViewSet(mixins.RelativeURLFieldMixin, viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = serializers.AccountSerializer

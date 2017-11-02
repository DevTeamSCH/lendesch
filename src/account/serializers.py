from django.contrib.auth.models import User
from rest_framework import serializers


class AccountSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        fields = ('url', 'first_name', 'last_name')
        model = User

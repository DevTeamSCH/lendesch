from rest_framework import serializers

from . import models


class LoanSerializer(serializers.HyperlinkedModelSerializer):
    remarks = serializers.HyperlinkedRelatedField(many=True, view_name='remark-detail', read_only=True)
    class Meta:
        fields = serializers.ALL_FIELDS
        model = models.Loan


class ResourceSerializer(serializers.HyperlinkedModelSerializer):
    remarks = serializers.HyperlinkedRelatedField(many=True, view_name='remark-detail', read_only=True)
    class Meta:
        fields = serializers.ALL_FIELDS
        model = models.Resource


class ResourceTypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        fields = serializers.ALL_FIELDS
        model = models.ResourceType


class RemarkSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'url', 'title', 'description', 'owner', 'created_at', 'updated_at',
            'object_id', 'content_type'
        )
        model = models.Remark

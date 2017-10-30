from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.fields import GenericRelation, GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from group.models import LenderGroup


class Remark(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    owner = models.ForeignKey(User, related_name='remarks', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # For generic relations
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    def __str__(self):
        return self.title


class ResourceType(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name


class Resource(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    owner = models.ForeignKey(LenderGroup, related_name='resources', on_delete=models.CASCADE)
    type_of = models.ForeignKey(ResourceType, related_name='resources', on_delete=models.CASCADE)
    remarks = GenericRelation(Remark)

    def __str__(self):
        return self.name


class Loan(models.Model):
    what = models.ForeignKey(Resource, related_name='loans', on_delete=models.CASCADE)
    reason = models.TextField()
    borrower = models.ForeignKey(User, related_name='loans', on_delete=models.CASCADE)
    when = models.DateTimeField()
    till = models.DateTimeField()
    back = models.DateTimeField()
    released = models.BooleanField()
    comment = models.TextField()
    remarks = GenericRelation(Remark)

    def __str__(self):
        return "{} {}".format(self.when, self.what)

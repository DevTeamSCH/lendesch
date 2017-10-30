from django.db import models
from django.contrib.auth.models import User


class ResourceType(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()


class Resource(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    owner = models.ForeignKey(User, related_name='resources')
    type_of = models.ForeignKey(ResourceType, related_name='resources')

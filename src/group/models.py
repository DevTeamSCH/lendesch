from django.db import models
from django.contrib.auth.models import User


class Group(models.Model):
    name = models.CharField(max_length=255)
    administrators = models.ManyToManyField(User, related_name='lenders')
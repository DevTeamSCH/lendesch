from django.contrib.auth.models import User
from django.db import models

from group.models import LenderGroup


class Constraint(models.Model):
    name = models.CharField(max_length=255)
    group = models.ForeignKey(LenderGroup, related_name='constraints', on_delete=models.CASCADE)
    fullfield = models.ManyToManyField(User, related_name='constraints', blank=True)

    class Meta:
        unique_together = ('name', 'group')

    def __str__(self):
        return self.name

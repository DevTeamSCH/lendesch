# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-02 22:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('constraint', '0001_initial'),
        ('loan', '0002_auto_20171030_2327'),
    ]

    operations = [
        migrations.AddField(
            model_name='resource',
            name='constraints',
            field=models.ManyToManyField(related_name='resources', to='constraint.Constraint'),
        ),
    ]

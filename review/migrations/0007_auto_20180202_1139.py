# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-02-02 11:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0006_auto_20180201_2012'),
    ]

    operations = [
        migrations.AddField(
            model_name='review_data',
            name='feedback',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='review_data',
            name='review',
            field=models.TextField(blank=True, null=True),
        ),
    ]

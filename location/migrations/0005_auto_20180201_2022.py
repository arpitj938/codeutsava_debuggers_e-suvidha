# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-02-01 20:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('location', '0004_location_data_review_count'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location_data',
            name='infrastructure',
            field=models.FloatField(blank=True, null=True),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-02-01 19:49
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('incharge', '0002_auto_20180201_1924'),
    ]

    operations = [
        migrations.AlterField(
            model_name='incharge_data',
            name='location_allocated',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='location.location_data'),
        ),
    ]

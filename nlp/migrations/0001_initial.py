# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-02-04 03:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='nlp_data',
            fields=[
                ('nlp_id', models.AutoField(primary_key=True, serialize=False)),
                ('review', models.CharField(blank=True, max_length=500, null=True)),
                ('problem', models.CharField(blank=True, max_length=500, null=True)),
            ],
        ),
    ]
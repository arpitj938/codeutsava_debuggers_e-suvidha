# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-02-01 18:32
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('location', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='incharge_data',
            fields=[
                ('incharge_id', models.IntegerField(primary_key=True, serialize=False)),
                ('incharge_name', models.CharField(max_length=200)),
                ('incharge_phone', models.CharField(max_length=10)),
                ('incharge_email', models.EmailField(max_length=254)),
                ('location_alloated', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='location.location_data')),
            ],
        ),
    ]

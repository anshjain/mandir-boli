# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-08-24 06:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_auto_20180715_1334'),
    ]

    operations = [
        migrations.AlterField(
            model_name='events',
            name='description',
            field=models.TextField(max_length=1500, verbose_name='Event Description'),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-09-23 12:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mandir', '0015_auto_20180812_1001'),
    ]

    operations = [
        migrations.AddField(
            model_name='record',
            name='remaining_amt',
            field=models.IntegerField(default=0, verbose_name='amount'),
        ),
    ]

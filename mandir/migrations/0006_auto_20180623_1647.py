# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-06-23 16:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mandir', '0005_auto_20180623_1643'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mandir',
            name='state',
            field=models.CharField(default='maharashtra', max_length=20, verbose_name='state'),
        ),
    ]

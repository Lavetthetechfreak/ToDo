# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-02 12:16
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('to_do_list', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2017, 5, 2, 12, 16, 21, 962718)),
        ),
    ]

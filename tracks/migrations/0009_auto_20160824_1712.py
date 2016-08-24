# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-24 17:12
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('tracks', '0008_auto_20160824_1711'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='date',
            field=models.DateField(default=datetime.datetime(2016, 8, 24, 17, 12, 7, 543418, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='project',
            name='date',
            field=models.DateField(default=datetime.datetime(2016, 8, 24, 17, 12, 7, 563167, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='track',
            name='date',
            field=models.DateField(default=datetime.datetime(2016, 8, 24, 17, 12, 7, 563728, tzinfo=utc)),
        ),
    ]

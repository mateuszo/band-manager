# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-24 20:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracks', '0014_auto_20160824_1953'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='status',
            field=models.CharField(choices=[('DRAFT', 'label-warning'), ('IN PROGRESS', 'label-info'), ('DONE', 'label-success'), ('OLD', 'label-default')], default='DRAFT', max_length=15),
        ),
    ]

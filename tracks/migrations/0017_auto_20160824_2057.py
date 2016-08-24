# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-24 20:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracks', '0016_auto_20160824_2053'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='status',
            field=models.CharField(choices=[('DRAFT', 'draft'), ('IN PROGRESS', 'in progress'), ('DONE', 'done'), ('OLD', 'old')], default='DRAFT', max_length=15),
        ),
    ]
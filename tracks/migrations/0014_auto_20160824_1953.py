# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-24 19:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracks', '0013_auto_20160824_1952'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='status',
            field=models.CharField(choices=[('DRAFT', {'css': 'label-warning', 'name': 'Zalążek'}), ('IN PROGRESS', {'css': 'label-info', 'name': 'W opracowaniu'}), ('DONE', {'css': 'label-success', 'name': 'Gotowy'}), ('OLD', {'css': 'label-default', 'name': 'Staroć'})], default={'css': 'label-warning', 'name': 'Zalążek'}, max_length=15),
        ),
    ]

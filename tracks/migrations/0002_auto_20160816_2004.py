# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-16 20:04
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tracks', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='track',
            old_name='Project',
            new_name='project',
        ),
    ]

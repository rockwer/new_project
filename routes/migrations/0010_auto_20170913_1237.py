# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-09-13 12:37
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('routes', '0009_auto_20170913_1230'),
    ]

    operations = [
        migrations.RenameField(
            model_name='city',
            old_name='name',
            new_name='title',
        ),
        migrations.RenameField(
            model_name='country',
            old_name='name',
            new_name='title',
        ),
    ]
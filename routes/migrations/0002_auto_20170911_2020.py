# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-09-11 17:20
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('routes', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Points',
            new_name='Point',
        ),
    ]

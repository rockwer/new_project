# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-09-13 16:13
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('points', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='country',
            old_name='flag',
            new_name='<django.db.models.fields.CharField><built-in function id>',
        ),
    ]

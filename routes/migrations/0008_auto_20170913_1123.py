# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-09-13 11:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('routes', '0007_point_coordinate'),
    ]

    operations = [
        migrations.RenameField(
            model_name='point',
            old_name='Coordinate',
            new_name='coordinate',
        ),
        migrations.RemoveField(
            model_name='photo',
            name='url',
        ),
        migrations.AddField(
            model_name='photo',
            name='image',
            field=models.ImageField(default='', upload_to='uploads/Photos'),
        ),
        migrations.AddField(
            model_name='point',
            name='adress',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='icon',
            name='image',
            field=models.ImageField(default='', upload_to='uploads/icons'),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-09-14 14:46
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('points', '0005_auto_20170913_1812'),
        ('routes', '0013_auto_20170914_1442'),
    ]

    operations = [
        migrations.AddField(
            model_name='edge',
            name='imp1',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='points.Importence'),
        ),
        migrations.AddField(
            model_name='edge',
            name='imp2',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='edge_edges_imp2', to='points.Importence'),
        ),
    ]

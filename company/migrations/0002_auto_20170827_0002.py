# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-08-26 18:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fundingdetail',
            name='stage',
            field=models.PositiveIntegerField(choices=[(1, 'Series A'), (2, 'Series B'), (3, 'Series C'), (4, 'Series D'), (5, 'Series E'), (6, 'Series F')]),
        ),
    ]

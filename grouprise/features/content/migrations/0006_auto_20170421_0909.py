# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-21 07:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("content2", "0005_auto_20170413_1203"),
    ]

    operations = [
        migrations.AlterField(
            model_name="content",
            name="all_day",
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name="content",
            name="place",
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name="content",
            name="time",
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="content",
            name="until_time",
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]

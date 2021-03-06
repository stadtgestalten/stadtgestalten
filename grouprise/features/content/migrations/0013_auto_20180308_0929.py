# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-03-08 08:29
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("content2", "0012_auto_20180222_1116"),
    ]

    operations = [
        migrations.AlterField(
            model_name="content",
            name="poll",
            field=models.OneToOneField(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="content",
                to="polls.WorkaroundPoll",
            ),
        ),
    ]

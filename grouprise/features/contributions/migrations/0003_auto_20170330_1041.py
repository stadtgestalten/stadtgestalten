# -*- coding: utf-8 -*-
# Generated by Django 1.11rc1 on 2017-03-30 08:41
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("contributions", "0002_auto_20170309_1515"),
    ]

    operations = [
        migrations.AlterField(
            model_name="contribution",
            name="author",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="contributions",
                to="gestalten.Gestalt",
            ),
        ),
    ]

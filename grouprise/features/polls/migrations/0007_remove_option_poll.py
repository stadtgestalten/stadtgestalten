# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-04 09:44
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("polls", "0006_auto_20180104_0936"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="option",
            name="poll",
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-07 11:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0007_remove_group_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='url_import_feed',
            field=models.BooleanField(default=False, verbose_name='Beiträge von Website übernehmen'),
        ),
    ]

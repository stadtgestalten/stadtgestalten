# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-15 08:35
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0010_auto_20160120_1501'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'ordering': ('-date_created',)},
        ),
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ('-date_created',)},
        ),
        migrations.AlterModelOptions(
            name='content',
            options={'ordering': ('-date_created',)},
        ),
        migrations.AlterModelOptions(
            name='event',
            options={'ordering': ('-date_created',)},
        ),
        migrations.AlterModelOptions(
            name='gallery',
            options={'ordering': ('-date_created',)},
        ),
    ]

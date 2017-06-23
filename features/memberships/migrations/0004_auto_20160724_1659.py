# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-24 14:59
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gestalten', '0001_initial'),
        ('memberships', '0003_auto_20160718_1404'),
    ]

    operations = [
        migrations.AlterField(
            model_name='membership',
            name='member',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestalten.Gestalt', verbose_name='Gestalt'),
        ),
    ]

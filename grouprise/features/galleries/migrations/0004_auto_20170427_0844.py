# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-27 06:44
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("content2", "0006_auto_20170421_0909"),
        ("images", "0002_auto_20170421_0911"),
        ("galleries", "0003_auto_20170421_1109"),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name="galleryimage",
            unique_together=set([("gallery", "image")]),
        ),
    ]

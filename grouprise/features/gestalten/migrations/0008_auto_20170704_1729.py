# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-04 15:29
from __future__ import unicode_literals

import grouprise.core.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("gestalten", "0007_remove_gestalt_addressed_content"),
    ]

    operations = [
        migrations.AlterField(
            model_name="gestalt",
            name="avatar",
            field=grouprise.core.models.ImageField(
                blank=True,
                help_text="Mögliche Formate sind JPEG, PNG und viele weitere. Nicht unterstützt werden PDF- oder SVG-Dateien. Die maximal erlaubte Dateigröße beträgt 5 MB.",
                upload_to="",
            ),
        ),
        migrations.AlterField(
            model_name="gestalt",
            name="background",
            field=grouprise.core.models.ImageField(
                blank=True,
                help_text="Mögliche Formate sind JPEG, PNG und viele weitere. Nicht unterstützt werden PDF- oder SVG-Dateien. Die maximal erlaubte Dateigröße beträgt 5 MB.",
                upload_to="",
                verbose_name="Hintergrundbild",
            ),
        ),
    ]

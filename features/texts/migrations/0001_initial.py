# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-10 15:17
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('gestalten', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Text',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('container_id', models.PositiveIntegerField()),
                ('time_created', models.DateTimeField(default=django.utils.timezone.now)),
                ('text', models.TextField()),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestalten.Gestalt')),
                ('container_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType')),
            ],
        ),
    ]

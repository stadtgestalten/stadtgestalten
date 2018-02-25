# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-02-22 09:33
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0013_auto_20180109_1302'),
    ]

    operations = [
        migrations.CreateModel(
            name='WorkaroundPoll',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('condorcet', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AlterModelOptions(
            name='option',
            options={'ordering': ('id',)},
        ),
        migrations.AlterModelOptions(
            name='vote',
            options={'ordering': ('time_updated',)},
        ),
        migrations.AddField(
            model_name='option',
            name='poll_new1',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='options_new', to='polls.WorkaroundPoll'),
        ),
    ]

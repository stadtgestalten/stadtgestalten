# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-09 13:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0033_merge_20170116_2223'),
    ]

    operations = [
        migrations.AlterField(
            model_name='content',
            name='public',
            field=models.BooleanField(default=False, help_text='Öffentliche Beiträge sind auch für Besucher_innen sichtbar, die nicht Mitglied der Gruppe sind', verbose_name='Öffentlich'),
        ),
        migrations.AlterField(
            model_name='event',
            name='all_day',
            field=models.BooleanField(default=False, help_text='Das Ereignis wird den gesamten Tag dauern', verbose_name='ganztägig'),
        ),
        migrations.AlterField(
            model_name='event',
            name='place',
            field=models.CharField(max_length=255, verbose_name='Veranstaltungsort / Anschrift'),
        ),
        migrations.AlterField(
            model_name='event',
            name='time',
            field=models.DateTimeField(verbose_name='Beginn'),
        ),
        migrations.AlterField(
            model_name='event',
            name='until_time',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Ende'),
        ),
    ]

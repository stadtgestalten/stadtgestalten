# Generated by Django 2.1.8 on 2019-04-07 22:27

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0002_auto_20180607_1128"),
    ]

    operations = [
        migrations.AlterField(
            model_name="permissiontoken",
            name="time_created",
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]

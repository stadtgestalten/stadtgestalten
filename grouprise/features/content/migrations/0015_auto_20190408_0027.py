# Generated by Django 2.1.8 on 2019-04-07 22:27

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("content2", "0014_auto_20181120_1512"),
    ]

    operations = [
        migrations.AlterField(
            model_name="version",
            name="time_created",
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]

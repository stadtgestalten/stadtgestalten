# Generated by Django 2.1.8 on 2019-04-07 22:27

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("memberships", "0015_auto_20180109_1302"),
    ]

    operations = [
        migrations.AlterField(
            model_name="membership",
            name="date_joined",
            field=models.DateField(default=datetime.date.today),
        ),
    ]

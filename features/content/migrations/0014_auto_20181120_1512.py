# Generated by Django 2.1.3 on 2018-11-20 14:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('content2', '0013_auto_20180308_0929'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='version',
            options={'ordering': ('time_created',)},
        ),
    ]

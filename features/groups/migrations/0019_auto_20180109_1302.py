# Generated by Django 2.0.1 on 2018-01-09 12:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0018_auto_20171128_0856'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='gestalt_created',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='gestalten.Gestalt'),
        ),
    ]
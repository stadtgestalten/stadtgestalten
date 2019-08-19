# Generated by Django 2.1.11 on 2019-08-15 07:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gestalten', '0013_gestalt_activity_bookmark_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gestaltsetting',
            name='gestalt',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='settings', to='gestalten.Gestalt'),
        ),
    ]
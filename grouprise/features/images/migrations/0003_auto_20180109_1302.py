# Generated by Django 2.0.1 on 2018-01-09 12:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("images", "0002_auto_20170421_0911"),
    ]

    operations = [
        migrations.AlterField(
            model_name="image",
            name="creator",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT,
                related_name="images",
                to="gestalten.Gestalt",
            ),
        ),
    ]

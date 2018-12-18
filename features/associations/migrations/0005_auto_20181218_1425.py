# Generated by Django 2.1.4 on 2018-12-18 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('associations', '0004_association_deleted'),
    ]

    operations = [
        migrations.AlterField(
            model_name='association',
            name='public',
            field=models.BooleanField(default=False, help_text='Öffentliche Beiträge sind auch für Besucherinnen sichtbar, die nicht Mitglied der Gruppe sind. Benachrichtigungen werden an Mitglieder und Abonnentinnen versendet.', verbose_name='Öffentlich'),
        ),
    ]

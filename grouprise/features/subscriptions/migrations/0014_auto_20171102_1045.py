# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-02 09:45
from __future__ import unicode_literals

from django.db import migrations
from django.db.transaction import atomic
from django.db.utils import IntegrityError


def add_subscriptions_for_memberships(apps, schema_editor):
    ContentType = apps.get_model("contenttypes", "ContentType")
    Membership = apps.get_model("memberships", "Membership")
    Subscription = apps.get_model("subscriptions", "Subscription")
    for membership in Membership.objects.all():
        try:
            with atomic():
                Subscription.objects.create(
                    subscribed_to_id=membership.group.id,
                    subscribed_to_type=ContentType.objects.get_for_model(
                        membership.group
                    ),
                    subscriber=membership.member,
                )
        except IntegrityError:
            pass


class Migration(migrations.Migration):

    dependencies = [
        ("memberships", "0014_auto_20170609_1029"),
        ("subscriptions", "0013_auto_20170918_1340"),
    ]

    operations = [
        migrations.RunPython(add_subscriptions_for_memberships),
    ]

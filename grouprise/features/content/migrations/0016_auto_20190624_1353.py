# Generated by Django 2.1.9 on 2019-06-24 11:53

from django.contrib.contenttypes.models import ContentType
from django.db import migrations
from taggit.managers import _TaggableManager
from taggit.models import Tag, TaggedItem


def copy_tags(apps, schema_editor):
    Content = apps.get_model("content2", "Content")
    Tagged = apps.get_model("tags", "Tagged")
    for tagged in Tagged.objects.all():
        if tagged.tagged_type == ContentType.objects.get_for_model(Content):
            content = Content.objects.get(id=tagged.tagged_id)
            tag, _ = Tag.objects.get_or_create(
                name=tagged.tag.name, slug=tagged.tag.slug
            )
            mgr = _TaggableManager(
                through=TaggedItem,
                model=Content,
                instance=content,
                prefetch_cache_name="tags",
            )
            mgr.add(tag)


class Migration(migrations.Migration):

    dependencies = [
        ("content2", "0015_auto_20190408_0027"),
        ("taggit", "0002_auto_20150616_2121"),
        ("tags", "0010_auto_20170622_1655"),
    ]

    operations = [
        migrations.RunPython(copy_tags),
    ]

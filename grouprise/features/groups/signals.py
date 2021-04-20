import json
import logging
import shlex
import subprocess

from django.conf import settings
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from huey.contrib.djhuey import db_task

from grouprise.core.utils import slugify
from grouprise.features.gestalten import models as gestalten
from grouprise.features.stadt.forms import ENTITY_SLUG_BLACKLIST
from .models import Group
from ...core.models import get_unique_slug

logger = logging.getLogger(__name__)


@db_task()
def call_hook_script(event_type: str, group: Group, timeout=300):
    hook_event_info_json = json.dumps(
        {
            "eventType": event_type,
            "objectType": "Group",
            "objectData": {"id": group.id, "slug": group.slug},
        }
    )
    hook_script_names = settings.GROUPRISE.get("HOOK_SCRIPT_PATHS", [])
    for script_name in hook_script_names:
        try:
            subprocess.run(
                [script_name, hook_event_info_json],
                check=True,
                capture_output=True,
                timeout=timeout,
            )
        except FileNotFoundError:
            logger.error("Configured hook script does not exist: %s", script_name)
        except PermissionError:
            logger.error(
                "Configured hook script is not accessible or not executable: %s",
                script_name,
            )
        except subprocess.CalledProcessError as exc:
            logger.error(
                "Hook script failed with a non-zero exitcode (%d): %s %s -> %s",
                exc.returncode,
                script_name,
                shlex.quote(hook_event_info_json),
                exc.stderr,
            )
        except subprocess.TimeoutExpired:
            logger.error(
                "Configured hook script failed to return within %d seconds: %s",
                timeout,
                script_name,
            )
        else:
            logger.info(
                "Hook script finished successfully: %s %s",
                script_name,
                shlex.quote(hook_event_info_json),
            )


@receiver(post_save, sender=Group)
def post_group_save(sender, instance, created, **kwargs):
    if created:
        call_hook_script("created", instance)
    else:
        call_hook_script("changed", instance)

    if created:
        instance.slug = get_unique_slug(
            Group,
            {"slug": slugify(instance.name)},
            reserved_slugs=ENTITY_SLUG_BLACKLIST,
            reserved_slug_qs=gestalten.Gestalt.objects,
            reserved_slug_qs_field="user__username",
        )
        instance.save()


@receiver(post_delete, sender=Group)
def group_deleted(sender, instance, **kwargs):
    call_hook_script("deleted", instance)

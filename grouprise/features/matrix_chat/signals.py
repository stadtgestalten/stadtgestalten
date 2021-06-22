import asyncio
import logging

from django.db.models.signals import post_delete, post_save
from django.dispatch import receiver
from huey.contrib.djhuey import db_task

from grouprise.core.templatetags.defaultfilters import full_url
import grouprise.features.content.models
import grouprise.features.contributions.models
import grouprise.features.groups.models
import grouprise.features.memberships.models
from .matrix_bot import MatrixBot, MatrixError
from .models import MatrixChatGroupRoom


logger = logging.getLogger(__name__)


@receiver(post_save, sender=grouprise.features.groups.models.Group)
def update_matrix_rooms_for_group(sender, instance, created, **kwargs):
    if created:
        _sync_rooms_delayed(instance)


@db_task()
def _sync_rooms_delayed(group):
    async def _sync_rooms_async(group):
        async with MatrixBot() as bot:
            try:
                await bot.synchronize_rooms_of_group(group)
            except MatrixError as exc:
                logger.warning(
                    f"Failed to synchronize group ({group}) with matrix rooms: {exc}"
                )

    asyncio.run(_sync_rooms_async(group))


@db_task()
def send_matrix_room_messages(messages):
    async def _send_room_messages_async(messages):
        async with MatrixBot() as bot:
            for group, message, is_public in messages:
                for room in MatrixChatGroupRoom.objects.filter(group=group):
                    # send private messages only to the internal room
                    if is_public or room.is_private:
                        try:
                            await bot.send_text(room, message)
                        except MatrixError as exc:
                            logger.warning(
                                f"Failed to send matrix notification for contribution: {exc}"
                            )

    asyncio.run(_send_room_messages_async(messages))


@receiver(post_save, sender=grouprise.features.content.models.Content)
def send_content_notification_to_matrix_rooms(sender, instance, created, **kwargs):
    # For unknown reasons the instance is not complete at this moment
    # ("instance.get_associated_groups()" is empty).  Thus we delay the execution slightly by
    # asking our worker process to process the instance when it is ready.
    _delayed_send_content_notification_to_matrix_rooms(instance, created)


@db_task()
def _delayed_send_content_notification_to_matrix_rooms(instance, created):
    # only sent group messages to matrix rooms
    if instance.get_associated_groups():
        version = instance.versions.last()
        author = version.author
        if instance.is_event:
            content_type = "Termin"
        elif instance.is_file:
            content_type = "Anhang"
        elif instance.is_gallery:
            content_type = "Galerie"
        elif instance.is_poll:
            content_type = "Umfrage"
        elif instance.is_conversation:
            content_type = "Gespräch"
        else:
            content_type = "Artikel"
        change_type = "neu" if created else "aktualisiert"
        messages = []
        for association in instance.associations.all():
            if association.entity.is_group:
                group = association.entity
                url = full_url(association.get_absolute_url())
                summary = f"{content_type} ({change_type}): [{instance.subject} ({author})]({url})"
                messages.append((group, summary, association.public))
        send_matrix_room_messages(messages)


@receiver(post_save, sender=grouprise.features.contributions.models.Contribution)
def send_contribution_notification_to_matrix_rooms(sender, instance, created, **kwargs):
    if not created:
        # send notifications only for new contributions
        pass
    elif instance.deleted:
        # ignore deleted contributions
        pass
    elif not instance.container.get_associated_groups():
        # only sent group messages to matrix rooms
        pass
    else:
        author = instance.author
        messages = []
        for association in instance.container.associations.all():
            if association.entity.is_group:
                group = association.entity
                url = full_url(association.get_absolute_url())
                summary = f"Diskussionsbeitrag: [{instance.container.subject} ({author})]({url})"
                messages.append((group, summary, instance.public))
        send_matrix_room_messages(messages)


@receiver(post_save, sender=grouprise.features.memberships.models.Membership)
def synchronize_matrix_room_memberships(sender, instance, created, **kwargs):
    if created:
        _invite_to_group_rooms(instance.group)


@db_task()
def _invite_to_group_rooms(group):
    async def _invite_to_group_rooms_delayed(group):
        async with MatrixBot() as bot:
            try:
                async for invited in bot.send_invitations_to_group_members(group):
                    logger.info(f"Invitation sent: {invited}")
            except MatrixError as exc:
                logger.warning(
                    f"Failed to invite new group members ({group}) to matrix rooms: {exc}"
                )

    asyncio.run(_invite_to_group_rooms_delayed(group))


@receiver(post_delete, sender=grouprise.features.memberships.models.Membership)
def kick_room_members_after_leaving_group(sender, instance, **kwargs):
    _kick_gestalt_from_group_rooms(instance.group, instance.member)


@db_task()
def _kick_gestalt_from_group_rooms(group, gestalt):
    async def _kick_gestalt_from_group_rooms_delayed(group, gestalt):
        async with MatrixBot() as bot:
            try:
                await bot.kick_gestalt_from_group_rooms(group, gestalt)
            except MatrixError as exc:
                logger.warning(
                    f"Failed to kick previous group members ({group}) from matrix rooms: {exc}"
                )

    asyncio.run(_kick_gestalt_from_group_rooms_delayed(group, gestalt))
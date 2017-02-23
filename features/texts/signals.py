from . import models
from django_mailbox import signals
from django import dispatch
from django.conf import settings


@dispatch.receiver(signals.message_received)
def process_message(sender, message, **args):
    token_beg = len(settings.DEFAULT_REPLY_TO_EMAIL.split('{')[0])
    token_end = len(settings.DEFAULT_REPLY_TO_EMAIL.rsplit('}')[1])
    token = message.to_addresses[0][token_beg:-token_end]
    key = models.ReplyKey.objects.get(key=token)
    models.Text.objects.create(
            author=key.gestalt, container=key.text.container, text=message.text)
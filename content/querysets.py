import datetime
from django.db import models
from django.utils import timezone
from features.groups import models as groups


class ContentQuerySet(models.QuerySet):
    def can_view(self, user):
        if user.is_authenticated():
            return self.filter(
                    models.Q(public=True) |
                    models.Q(author=user.gestalt) |
                    models.Q(groupcontent__group__in=groups.Group.objects.filter(
                        memberships__member=user.gestalt)) |
                    models.Q(gestaltcontent__gestalt=user.gestalt)
                    )
        else:
            return self.public()

    def permitted(self, user):
        return self.can_view(user)

    def public(self):
        return self.filter(public=True)


class EventQuerySet(ContentQuerySet):
    def around(self, time=timezone.now()):
        delta = datetime.timedelta(weeks=6)
        return self.filter(time__gt=time-delta, time__lt=time+delta)

    def upcoming(self, count=None):
        return self.filter(time__gte=timezone.now())[:count]
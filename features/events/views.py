import django.utils.timezone
import django.views.generic
from django.core.urlresolvers import reverse
from django.views import generic

import core.views
from utils import views as utils_views
import features.content.views
from features.associations import models as associations
from features.memberships.rules import is_member_of
from content import views as content_views


class List(core.views.PermissionMixin, django.views.generic.ListView):
    permission_required = 'events.view_list'
    model = associations.Association
    template_name = 'events/list.html'
    paginate_by = 10

    def get_content(self):
        return associations.Association.objects.can_view(self.request.user)

    def get_queryset(self):
        return super().get_queryset().filter_events().filter_upcoming().can_view(
                self.request.user).order_by('content__time')


class Create(features.content.views.Create):
    template_name = 'events/create.html'

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['with_time'] = True
        return kwargs


class GroupCalendarFeed(content_views.BaseCalendarFeed, features.groups.views.Mixin):

    def items(self):
        filter_dict = {'groups': self.get_group(),
                       'public': (self.kwargs['domain'] == "public")}
        return super().items().filter(**filter_dict)

    def get_calendar_owner(self):
        return self.get_group()

    def check_authorization(self, authenticated_gestalt):
        return ((authenticated_gestalt is not None)
                and is_member_of(authenticated_gestalt.user, self.get_group()))


class CalendarExport(utils_views.PageMixin, generic.DetailView):
    sidebar = tuple()
    template_name = 'events/export.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['public_export_url'] = self.request.build_absolute_uri(
            reverse(self.feed_route, kwargs={
                self.slug_url_kwarg: self.get_object().slug,
                'domain': 'public'
            })
        )
        if self.has_private_access():
            relative_url = reverse(self.feed_route,
                                   kwargs={self.slug_url_kwarg: self.get_object().slug,
                                           'domain': 'private'})
            user_resolver = content_views.BaseCalendarFeed.user_resolver
            url_with_token = user_resolver.get_url_with_permission_token(
                self.get_object(), self.request.user.gestalt, relative_url)
            context['private_export_url'] = self.request.build_absolute_uri(url_with_token)
        return context


class GroupCalendarExport(CalendarExport):
    model = features.groups.models.Group
    slug_url_kwarg = 'group_slug'
    permission = 'entities.view_group'
    title = 'Exportmöglichkeiten für Gruppenkalender'
    parent = 'group'
    feed_route = 'group-events-feed'

    def get_parent(self):
        return self.get_group()

    def has_private_access(self):
        if self.request.user and self.request.user.is_authenticated():
            return is_member_of(self.request.user, self.get_group())
        else:
            return False

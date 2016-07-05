from . import models
import rules

@rules.predicate
def is_gestalt(user, gestalt):
    return gestalt and user == gestalt.user

@rules.predicate
def is_group_member(user, group):
    if type(group) == models.GroupAttention:
        group = group.group
    return group and group.members.filter(user=user).exists()

@rules.predicate
def is_group_membership(user, membership):
    return membership and user and membership.gestalt == user.gestalt if membership else False

@rules.predicate
def is_public(user, gestalt):
    return gestalt.public

rules.add_perm('entities.view_gestalt', is_public | is_gestalt)
rules.add_perm('entities.change_gestalt', rules.is_authenticated & is_gestalt)
rules.add_perm('entities.create_gestalt_content', rules.is_authenticated & is_gestalt)
rules.add_perm('entities.create_gestalt_message', rules.always_allow)
rules.add_perm('entities.mail_gestalt', rules.is_authenticated & ~is_gestalt)

rules.add_perm('entities.view_group', rules.always_allow)
rules.add_perm('entities.create_group', rules.always_allow)
rules.add_perm('entities.change_group', rules.is_authenticated & is_group_member)
rules.add_perm('entities.create_group_content', rules.is_authenticated & is_group_member)
rules.add_perm('entities.create_group_message', rules.always_allow)
rules.add_perm('entities.create_membership', rules.is_authenticated & ~is_group_member)
rules.add_perm('entities.delete_membership', rules.is_authenticated & is_group_membership)
rules.add_perm('entities.list_members', rules.is_authenticated & is_group_member)

rules.add_perm('entities.view_imprint', rules.always_allow)

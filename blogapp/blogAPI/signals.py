from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User, Group


@receiver(post_save, sender=User)
def add_user_to_default_group(sender, instance, created, **kwargs):
    if created:
        default_group = Group.objects.get(name='User')
        instance.groups.add(default_group)
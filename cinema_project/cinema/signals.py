from django.contrib.auth.models import User, Group
from django.db.models.signals import m2m_changed
from django.dispatch import receiver

@receiver(m2m_changed, sender=User.groups.through)
def update_staff_status(sender, instance, action, **kwargs):
    staff_groups = ['Касир', 'Адміністратор', 'Директор']
    if action in ['post_add', 'post_remove', 'post_clear']:
        if instance.groups.filter(name__in=staff_groups).exists():
            instance.is_staff = True
        else:
            instance.is_staff = False
        instance.save()

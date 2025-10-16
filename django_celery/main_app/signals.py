from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import User
from .tasks import send_verification_email


@receiver(post_save, sender=User)
def user_update(sender, instance, *args, **kwargs):
    if not instance.is_verified:
        send_verification_email.delay(instance.pk)

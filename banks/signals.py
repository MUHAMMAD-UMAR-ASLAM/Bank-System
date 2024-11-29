from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Account


@receiver(post_save, sender=Account)
def account_created(sender, instance, created, **kwargs):
    if created:
        print(f"Account created for {instance.user.username}")

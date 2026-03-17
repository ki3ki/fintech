# transactions/signals.py

from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Transaction
from .ai_service import categorize_transaction

@receiver(post_save, sender=Transaction)
def classify_transaction(sender, instance, created, **kwargs):
    if created and not instance.category:
        instance.category = categorize_transaction(instance.description)
        instance.save()
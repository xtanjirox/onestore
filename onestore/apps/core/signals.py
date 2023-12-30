from django.db.models.signals import post_save
from django.dispatch import receiver
from onestore.apps.core import models


@receiver(post_save, sender=models.ExampleModel)
def signal_example(sender, instance, created, **kwargs):
    if created:
        return True

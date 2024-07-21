from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone
from .models import OperatingRoomSchedule

@receiver(post_save, sender=OperatingRoomSchedule)
def handle_schedule_post_save(sender, instance, **kwargs):
    if instance.is_expired():
        instance.release_operating_room()
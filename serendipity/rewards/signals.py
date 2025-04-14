from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.timezone import now
from .models import ScheduledReward
from .tasks import delayed_reward


@receiver(post_save, sender=ScheduledReward)
def schedule_task_on_create(sender, instance, created, **kwargs):
    if created:
        eta = instance.execute_at
        if eta > now():
            delayed_reward.apply_async(args=[instance.id], eta=eta)

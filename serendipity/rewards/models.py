from django.core.exceptions import ValidationError
from django.utils import timezone
from django.db import models
from accounts.models import RewardedUser


class ScheduledReward(models.Model):
    user = models.ForeignKey(RewardedUser, on_delete=models.CASCADE, blank=False)
    amount = models.IntegerField(blank=False)
    execute_at = models.DateTimeField(blank=False)

    def clean(self):
        super().clean()
        if self.execute_at <= timezone.now():
            raise ValidationError({'execute_at': 'Date must be in the future.'})


class RewardLog(models.Model):
    user = models.ForeignKey(RewardedUser, on_delete=models.CASCADE, blank=False)
    amount = models.IntegerField(blank=False)
    given_at = models.DateTimeField(auto_now_add=True)

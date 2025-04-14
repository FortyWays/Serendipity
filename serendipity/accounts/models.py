from django.contrib.auth.models import AbstractUser
from django.db import models


class RewardedUser(AbstractUser):
    coins = models.IntegerField(blank=True, default=0)

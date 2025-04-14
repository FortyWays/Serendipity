from celery import shared_task
from .models import ScheduledReward, RewardLog


@shared_task
def delayed_reward(reward_id):
    reward = ScheduledReward.objects.get(id=reward_id)
    user = reward.user
    user.coins += reward.amount
    user.save()
    log = RewardLog(user=user, amount=reward.amount)
    log.save()
    print(f"Giving out rewards({reward.amount}) to the lucky user: {user}!")

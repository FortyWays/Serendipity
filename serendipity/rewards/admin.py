from django.contrib import admin
from .models import ScheduledReward, RewardLog


@admin.register(RewardLog)
class RewardLogAdmin(admin.ModelAdmin):

    fields = ['user', 'amount', 'given_at']

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


admin.site.register(ScheduledReward)

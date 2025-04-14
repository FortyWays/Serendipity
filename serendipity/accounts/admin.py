from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import RewardedUser


class RewardedUserAdmin(UserAdmin):
    model = RewardedUser

    fieldsets = UserAdmin.fieldsets + (
        ("Serendipity Fields", {
            "fields": ("coins",),
        }),
    )

    add_fieldsets = UserAdmin.add_fieldsets + (
        ("Serendipity Fields", {
            "fields": ("coins",),
        }),
    )

    list_display = ("username", "email", "coins")


admin.site.register(RewardedUser, RewardedUserAdmin)

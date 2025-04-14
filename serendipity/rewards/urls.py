from django.urls import path
from .views import DailyRewardRequestView, RewardLogListView


urlpatterns = [
    path('', RewardLogListView.as_view()),
    path('request/', DailyRewardRequestView.as_view())
]

from django.urls import path
from .views import DailyRewardRequestView


urlpatterns = [
    path('request/', DailyRewardRequestView.as_view())
]

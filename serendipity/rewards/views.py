from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from .throttling import OncePerDayThrottle
from .models import ScheduledReward, RewardLog
from .serializers import RewardLogSerializer
from django.utils import timezone
from datetime import timedelta


class RewardLogListView(ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = RewardLogSerializer

    def get_queryset(self):
        return RewardLog.objects.filter(user=self.request.user)
    

class DailyRewardRequestView(APIView):
    permission_classes = [IsAuthenticated]
    throttle_classes = [OncePerDayThrottle]

    def post(self, request):
        amount = request.data.get('amount')

        if not amount:
            return Response(
                {"error": "Missing 'message' field in request."},
                status=status.HTTP_400_BAD_REQUEST
            )

        user = request.user
        reward = ScheduledReward(user=user,
                                 amount=amount,
                                 execute_at=timezone.now()+timedelta(minutes=5))
        reward.save()
        return Response({"message": f"Received your request, {user.username}!" +
                        "Your reward will be given out in 5 minutes"},
                        status=status.HTTP_200_OK)

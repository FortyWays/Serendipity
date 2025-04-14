from rest_framework.throttling import UserRateThrottle
from rest_framework.exceptions import Throttled


class OncePerDayThrottle(UserRateThrottle):
    rate = '1/day'

    def allow_request(self, request, view):
        if not super().allow_request(request, view):
            duration = self.wait()
            raise Throttled(
                detail="You can only access this endpoint once per day.",
                wait=duration
            )
        return True

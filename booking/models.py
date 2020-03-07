from django.db import models
from hotels.models import Hotels, Room
from django.contrib.auth.models import User
from django.conf import settings

class Booking(models.Model):
    hotel = models.ForeignKey(Hotels, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    checkin = models.DateField()
    checkout = models.DateField()
    totalcost = models.IntegerField(default=0)

    def __str__(self):
        return self.user.email

from django.db import models
from hotels.models import Hotels, Room
from django.contrib.auth.models import User
from django.conf import settings
from wgwdearlife.utils import unique_booking_id_generator
from booking.choices import *
from django.db.models.signals import pre_save, post_save



class Booking(models.Model):
    hotel = models.ForeignKey(Hotels, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    invoice = models.CharField(max_length=120, blank=True)
    status = models.CharField(max_length=120, default = 'Requested', choices=APPLY_STATUS_CHOICES)
    creation_date = models.DateTimeField(auto_now=True)
    checkin = models.DateField()
    checkout = models.DateField()
    room_booked = models.IntegerField(default=0)
    totalcost = models.IntegerField(default=0)
    def __str__(self):
        return str(self.user)

# def pre_save_create_booking_id(sender, instance, *args, **kwargs):
#     if not instance.booking_id:
#         instance.booking_id = unique_booking_id_generator(instance)



# pre_save.connect(pre_save_create_booking_id, sender=Booking)



class Notification(models.Model):
    receiver = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    message = models.CharField(max_length=255, blank=True, null=True)
    is_read = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now=True, auto_now_add=False, blank=True)

    def __str__(self):
        return str(self.message)

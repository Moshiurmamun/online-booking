from django.db import models
from django.urls import reverse
from accounts.models import UserProfile



def upload_location(instance, filename):
    return "%s/%s" %(instance.id, filename)


class HotelsManager(models.Manager):
    def active(self, *args, **kwargs):
        return super(HotelsManager, self).filter(draft=False)

class Places(models.Model):
    name = models.CharField(max_length=255)
    country = models.CharField(max_length=255, null=True, blank=True)
    image = models.ImageField(upload_to='places_image', null=True, blank=True)


    def __str__(self):
        return self.name





class Hotels(models.Model):
    name = models.CharField(max_length=255)
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    places = models.ForeignKey(Places ,on_delete=models.CASCADE, null=True, blank=True)
    address = models.CharField(max_length=255, null=True,blank=True)
    image = models.ImageField(upload_to='hotels_image', null=True, blank=True,)
    city = models.CharField(max_length=255,null=True,blank=True)
    telephone = models.CharField(max_length=255, null=True,blank=True)
    description = models.TextField(null=True, blank=True)
    rating = models.FloatField()
    draft = models.BooleanField(default=True)


    def __str__(self):
        return self.name

    objects = HotelsManager()




class Room(models.Model):
    name = models.CharField(max_length=255)
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    hotel = models.ForeignKey(Hotels, on_delete=models.CASCADE, null=True, blank=True)
    roomtype = models.CharField(max_length=255, null=True, blank=True)
    image = models.ImageField(upload_to='rooms_image', null=True, blank=True,)
    capacity = models.CharField(max_length=255, null=True, blank=True)
    price = models.FloatField(default=0)
    quantity = models.IntegerField(null=True, blank=True)
    discount = models.FloatField(default=0, null=True, blank=True)
    vat = models.FloatField(default=0, null=True, blank=True)
    service_charge = models.FloatField(default=0, null=True, blank=True)

    def __str__(self):
        return self.name

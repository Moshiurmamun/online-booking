from django.db import models
from django.urls import reverse

def upload_location(instance, filename):
    return "%s/%s" %(instance.id, filename)



class Room(models.Model):
    name = models.CharField(max_length=255)
    roomtype = models.CharField(max_length=255, null=True, blank=True)
    image = models.ImageField(upload_to='rooms_image', null=True, blank=True,)
    capacity = models.CharField(max_length=255, null=True, blank=True)
    price = models.FloatField(default=0)
    check_in = models.DateTimeField(auto_now=True)
    check_out = models.DateTimeField(auto_now=True)
    discount = models.FloatField(default=0, null=True, blank=True)
    vat = models.FloatField(default=0, null=True, blank=True)
    service_charge = models.FloatField(default=0, null=True, blank=True)

    def __str__(self):
        return self.name



class Hotels(models.Model):
    name = models.CharField(max_length=255)
    room = models.ManyToManyField(Room)
    address = models.CharField(max_length=255, null=True,blank=True)
    image = models.ImageField(upload_to='hotels_image', null=True, blank=True,)
    city = models.CharField(max_length=255,null=True,blank=True)
    telephone = models.CharField(max_length=255, null=True,blank=True)
    description = models.TextField(null=True, blank=True)
    rating = models.FloatField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("hotels:hotel_list", args=[self.id])




class Places(models.Model):
    name = models.CharField(max_length=255)
    hotels = models.ManyToManyField(Hotels)
    country = models.CharField(max_length=255, null=True, blank=True)
    image = models.ImageField(upload_to='places_image', null=True, blank=True,)

    def _str__(self):
        return self.name

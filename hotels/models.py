from django.db import models


class Places(models.Model):
    name = models.CharField(max_length=255)
    country = models.CharField(max_length=255)

    def _str__(self):
        return self.name


class Hotels(models.Model):
    place = models.ForeignKey(Places, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    telephone = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    rating = models.IntegerField()

    def __str__(self):
        return self.name

class Room(models.Model):
    hotel = models.ForeignKey(Hotels, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    roomtype = models.CharField(max_length=255)
    capacity = models.CharField(max_length=255)
    price = models.IntegerField(default=0)
    check_in = models.DateTimeField(auto_now=True)
    check_out = models.DateTimeField(auto_now=True)
    discount = models.IntegerField(default=0, null=True, blank=True)
    vat = models.IntegerField(default=0, null=True, blank=True)
    service_charge = models.IntegerField(default=0, null=True, blank=True)

    def __str__(self):
        return self.name






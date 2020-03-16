from django.db import models
from django.urls import reverse
from accounts.models import UserProfile

from django.db.models.signals import pre_save, post_save
from django.utils.text import slugify




def upload_location(instance, filename):
    return "%s/%s" %(instance.id, filename)


class HotelsManager(models.Manager):
    def active(self, *args, **kwargs):
        return super(HotelsManager, self).filter(draft=False)

class Places(models.Model):
    name = models.CharField(max_length=255)
    country = models.CharField(max_length=255, null=True, blank=True)
    image = models.ImageField(upload_to='places_image', null=True, blank=True)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name


    def get_absolute_url(self):
        return reverse('hotels:hotel_list', kwargs={"slug": self.slug})


    def _get_unique_slug(self):
        slug = slugify(self.name)
        unique_slug = slug
        num=1
        while Places.objects.filter(slug=unique_slug).exists():
            unique_slug = '{}-{}'.format(slug, num)
            num +=1
        return unique_slug

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self._get_unique_slug()
        super().save()



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
    slug = models.SlugField(unique=True, blank=True)


    def __str__(self):
        return self.name


    def save(self, *args, **kwargs):
        self.slug = '-'.join((slugify(self.places.name), slugify(self.name)))
        super(Hotels, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('hotels:room_list', kwargs={"slug": self.slug})



    objects = HotelsManager()



class Room(models.Model):
    name = models.CharField(max_length=255)
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE,null=True)
    hotel = models.ForeignKey(Hotels, on_delete=models.CASCADE, null=True, blank=True)
    roomtype = models.CharField(max_length=255, null=True, blank=True)
    image = models.ImageField(upload_to='rooms_image', null=True, blank=True,)
    capacity = models.CharField(max_length=255, null=True, blank=True)
    price = models.FloatField(default=0)
    quantity = models.IntegerField(null=True, blank=True)
    discount = models.FloatField(default=0, null=True, blank=True)
    vat = models.FloatField(default=0, null=True, blank=True)
    service_charge = models.FloatField(default=0, null=True, blank=True)
    slug = models.SlugField(unique=True, blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = '-'.join((slugify(self.hotel.name), slugify(self.name)))
        super(Room, self).save(*args, **kwargs)

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save


# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30, null=True, blank=True)
    last_name = models.CharField(max_length=30, null=True, blank=True)
    email = models.EmailField(max_length=254,null=True)
    phone = models.IntegerField(default=0)
    permanent_address = models.CharField(max_length=100,null=True, blank=True)
    present_address = models.CharField(max_length=100,null=True, blank=True)
    age = models.IntegerField( null=True,blank=True)

    def __str__(self):
        return self.user.username


def create_profile(sender, **kwargs):
    if kwargs['created']:
        user_profile = UserProfile.objects.create(user=kwargs['instance'])


post_save.connect(create_profile, sender=User)

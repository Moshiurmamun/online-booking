from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager




# user profile manager
class UserProfileManager(BaseUserManager):
    """Helps django work with our custom user model"""

    def create_user(self, email, phone=None, password=None, **kwargs):
        """creates a new user profile objecs"""

        if not email:
            raise ValueError('User must have an email address!')

        if not phone:
            raise ValueError('User must have an phone number!')

        email = self.normalize_email(email)
        user = self.model(email=email, phone=phone)

        user.set_password(password)
        user.save(using=self._db)

        return user


    def create_superuser(self, email, phone, password):
        """creates and saves a new super user with given details"""

        user = self.create_user(email=email, phone=phone, password=password)

        user.is_superuser = True
        user.is_staff = True

        user.save(using=self._db)

        return user



# user profile model
class UserProfile(AbstractBaseUser, PermissionsMixin):
    """Represents a user profile inside our system"""

    #basic info
    firstname = models.CharField(max_length=255, null=True, blank=True)
    lastname = models.CharField(max_length=255, null=True, blank=True)
    email = models.EmailField(max_length=255, unique=True)
    phone = models.CharField(max_length=255, null=True, blank=True)
    image = models.ImageField(upload_to='user_image', null=True, blank=True)
    address = models.CharField(max_length = 255, null=True, blank=True)
    country = models.CharField(max_length=40, null=True,blank=True)



    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['phone', ]


    def __str__(self):
        """Django uses this when it needs to convert the object to a string"""

        return self.email





class SocialAuthModelBackend(object):
    def authenticate(self, request, uid=None):
        try:
            social_user = SocialAuth.objects.get(uid=uid)
            return social_user.user
        except:
            return None

    def get_user(self, uid):
        try:
            social_user = SocialAuth.objects.get(uid=uid)
            return social_user.user
        except SocialAuth.DoesNotExist:
            return None


#facebook login
class SocialAuth(models.Model):
    user = models.OneToOneField(UserProfile, on_delete=models.CASCADE, null=True, blank=True)
    provider = models.CharField(max_length=255, default='Facebook', null=True, blank=True)
    uid = models.CharField(max_length=255, null=True, blank=True)
    access_token = models.TextField(max_length=2000, null=True, blank=True)

    def __str__(self):
        return str(self.uid)

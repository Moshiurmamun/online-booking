
from django.contrib import admin

from . import models


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['email','phone']

admin.site.register(models.UserProfile, UserProfileAdmin)
admin.site.site_header = "Dear Life Bd"

admin.site.register(models.SocialAuth)

from django.contrib import admin
from .models import Places,Hotels, Room

class PlaceModelAdmin(admin.ModelAdmin):
    list_display = ['name']
    prepopulated_fields = {'slug': ('name',)}

    class Meta:
        model = Places

admin.site.register(Places, PlaceModelAdmin)





admin.site.register(Hotels)


admin.site.register(Room)

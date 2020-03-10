from django.urls import path, re_path
from . import views



app_name = 'staff'

urlpatterns = [
    path('', views.staff_home, name = "staff_home"),

    #Places list and delete
    path('places/', views.places_list, name="places_list"),
    path('add-places/', views.add_places, name="add_places"),

    #Hotels list add and delete
    path('hotels/', views.hotels, name="hotels"),


    # Room List
    path('rooms/', views.rooms, name="rooms"),


    # Add hotels
    re_path('add-hotel/(?P<place_id>\d+)/$', views.addhotel, name="addhotel"),


    # Add room
    re_path('add-room/(?P<id>\d+)/$', views.add_room, name="add_room"),

]

from django.urls import path, re_path
from . import views



app_name = 'staff'

urlpatterns = [

    path('', views.staff_home, name = "staff_home"),


    path('view-booking', views.view_booking, name="view_booking"),

    #Places list and delete
    path('places/', views.places_list, name="places_list"),
    path('add-places/', views.add_places, name="add_places"),

    #Hotels list add and delete
    path('hotels/', views.hotels, name="hotels"),


    # Room List
    path('rooms/', views.rooms, name="rooms"),



    # Edit Places
    re_path('edit-places/(?P<id>\d+)/$',views.edit_places, name="edit_places"),



    # Add hotels , Edit Hotel
    re_path('add-hotel/(?P<place_id>\d+)/$', views.addhotel, name="addhotel"),
    re_path('edit-hotel/(?P<id>\d+)/$', views.edit_hotel, name="edit_hotel"),


    # Add room, Edit Room
    re_path('add-room/(?P<id>\d+)/$', views.add_room, name="add_room"),
    re_path('edit-room/(?P<id>\d+)/$', views.edit_room, name = "edit_room"),
]

from django.urls import path, re_path
from . import views
from django.contrib.auth.decorators import login_required


app_name = 'staff'

urlpatterns = [

    path('', login_required(views.staff_home), name = "staff_home"),


    path('view-booking', login_required(views.view_booking), name="view_booking"),

    #Places list and delete
    path('places/',login_required(views.places_list), name="places_list"),
    path('add-places/', login_required(views.add_places), name="add_places"),

    #Hotels list add and delete
    path('hotels/', login_required(views.hotels), name="hotels"),


    # Room List
    path('rooms/', login_required(views.rooms), name="rooms"),



    # Edit Places
    re_path('edit-places/(?P<id>\d+)/$', login_required(views.edit_places), name="edit_places"),



    # Add hotels , Edit Hotel
    re_path('add-hotel/(?P<place_id>\d+)/$', login_required(views.addhotel), name="addhotel"),
    re_path('edit-hotel/(?P<id>\d+)/$', login_required(views.edit_hotel), name="edit_hotel"),


    # Add room, Edit Room
    re_path('add-room/(?P<id>\d+)/$', login_required(views.add_room), name="add_room"),
    re_path('edit-room/(?P<id>\d+)/$', login_required(views.edit_room), name = "edit_room"),
]

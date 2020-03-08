from django.urls import path, re_path
from . import views
from hotels.views import hotelSearch

app_name = 'hotels'

urlpatterns = [
    path('', views.place_list, name='list'),
    path('search/', hotelSearch.as_view(), name='hotelsearch'),
    re_path('list/(?P<id>[0-9]+)/$', views.hotels_list, name='hotel_list' ),
    re_path('list/rooms/(?P<id>[0-9]+)/$', views.room_list, name ='room_list')

]

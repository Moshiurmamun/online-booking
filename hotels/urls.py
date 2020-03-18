from django.urls import path, re_path
from . import views
from hotels.views import hotelSearch

app_name = 'hotels'

urlpatterns = [
    path('', views.place_list, name='list'),
    path('dashboard/', views.userdash, name='userdash'),
    path('search/', hotelSearch.as_view(), name='hotelsearch'),
    re_path('list/(?P<slug>[-\w]+)/$', views.hotels_list, name='hotel_list' ),
    re_path('list/rooms/(?P<slug>[-\w]+)/$', views.room_list, name ='room_list')

]

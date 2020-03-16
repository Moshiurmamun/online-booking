from django.urls import path, re_path
from . import views



app_name = 'booking'

urlpatterns = [
   # path('book/mybooking/',views.mybooking, name="viewbookings"),
    re_path('book/(?P<hotelid>[0-9]+)/room/(?P<roomid>[0-9]+)/$', views.bookroom, name='bookroom'),
    #re_path("book/new/(?P<roomid>[0-9]+)/(?P<hotelid>[0-9]+)/(?P<checkin>(\d{4}-\d{2}-\d{2}))/(?P<checkout>(\d{4}-\d{2}-\d{2}))/(?P<totalcost>[0-9]+)$", views.storeBooking, name='newbooking'),
]

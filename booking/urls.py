from django.urls import path, re_path
from . import views
from .views import GeneratePDF


app_name = 'booking'

urlpatterns = [

    # ================================ User room booking list ==================================
    path('mybooking/',views.mybooking, name="viewbookings"),


    # ============= notification read view ======================
    path('notification/read', views.markAsRead, name="read"),

    re_path('book/(?P<hotelid>[0-9]+)/room/(?P<roomid>[0-9]+)$', views.bookroom, name='bookroom'),
    re_path("book/new/(?P<roomid>[0-9]+)/(?P<hotelid>[0-9]+)/(?P<checkin>(\d{4}-\d{2}-\d{2}))/(?P<checkout>(\d{4}-\d{2}-\d{2}))/(?P<room_no>[0-9]+)/(?P<totalcost>[0-9]+)$", views.storeBooking, name='newbooking'),
    re_path("mybooking/(?P<id>[0-9]+)/pdf$", GeneratePDF.as_view(), name='gpdf'),
    re_path("mybooking/cancel/(?P<id>[0-9]+)$", views.cancelbooking, name="cancelbooking"),
]

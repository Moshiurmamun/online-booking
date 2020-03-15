from django.urls import path
from . import views



app_name = 'booking'

urlpatterns = [
   # path('book/mybooking/',views.mybooking, name="viewbookings"),
    path('book/<hotelid>/room/<roomid>/', views.bookroom, name='bookroom'),

]

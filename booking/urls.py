from django.urls import path
from . import views



app_name = 'booking'

urlpatterns = [
    #path('book/mybooking/',views.mybooking, name="mybooking"),

    path('book/<hotelid>/<roomid>/', views.bookroom, name='bookroom'),

]

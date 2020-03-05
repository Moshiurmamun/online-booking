from django.urls import path
from . import views



app_name = 'booking'

urlpatterns = [
    path('book/<hotelid>/<roomid>/', views.bookroom, name='bookroom'),

]

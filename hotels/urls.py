from django.urls import path
from . import views


app_name = 'hotels'

urlpatterns = [
    path('', views.place_list, name='list'),
    path('list/<id>/', views.hotels_list, name='hotel_list' ),

]

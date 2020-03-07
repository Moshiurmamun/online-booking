from django.shortcuts import render, get_object_or_404
from .models import Places, Hotels, Room
from . import forms

def place_list(request):
    places = Places.objects.all()

    context = {
        'places': places,
    }
    return render(request, 'hotels/list.html', context )


def hotels_list(request, id):
    #instance = get_object_or_404(Places, id=id)
    instance = Places.objects.get(id=id)
    hotels = Hotels.objects.filter(places=instance)

    context = {
        'hotels': hotels,
    }


    for hotel in hotels:
        print(hotel.name)


    return render(request, 'hotels/hotel_list.html', context)

def room_list(request, id):



    thehotel = Hotels.objects.get(id=id)
    rooms = Room.objects.filter(hotel=thehotel)

    context = {
        'rooms': rooms,
        'hotel': thehotel,
    }
    return render(request, 'hotels/room_list.html', context)

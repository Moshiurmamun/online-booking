from django.shortcuts import render, get_object_or_404
from .models import Places, Hotels

def place_list(request):
    places = Places.objects.all()

    context = {
        'places': places,
    }
    return render(request, 'hotels/list.html', context )


def hotels_list(request, id):
    instance = get_object_or_404(Places, id=id)
    hotels = instance.hotels.all()

    #room list
    ins = get_object_or_404(Hotels, id=id)
    rooms = ins.room.all()

    context = {
        'hotels': hotels,
        'instance': instance,
        'rooms': rooms,

    }
    for hotel in hotels:
        print(hotel.name)

    for room in rooms:
        print(room.name)

    return render(request, 'hotels/hotel_list.html', context)


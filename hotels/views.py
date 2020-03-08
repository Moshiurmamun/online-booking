from django.shortcuts import render, get_object_or_404
from .models import Places, Hotels, Room
from . import forms
from django.views import generic
from django.views import View
from django.db.models import Q
from booking.models import Booking


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
        'instance': instance,
    }




    return render(request, 'hotels/hotel_list.html', context)

def room_list(request, id):

    """"
    form = BookingForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            if request.user.is_authenticated:
                booking = Booking()
                booking.checkin = form.cleaned_data.get('checkin')
                booking.checkout = form.cleaned_data.get('checkout')
                booking.save()
"""

    thehotel = Hotels.objects.get(id=id)
    rooms = Room.objects.filter(hotel=thehotel)



    FirstDate = request.session['checkin']
    SecDate =  request.session['checkout']

    for room in rooms:
        RoomsBooked = Booking.objects.filter(room=room).filter(checkin__lte = SecDate,
                                                               checkout__gte = FirstDate)
        count = RoomsBooked.count()
        count = int(count)
        Roomsavailable = room.quantity


        Roomsleft = Roomsavailable - count
        room.spaceleft = Roomsleft

    context = {
        'rooms': rooms,
        'hotel': thehotel,

    }
    return render(request, 'hotels/room_list.html', context)



class hotelSearch(View):
    def get(self, request):
        return render(request,'hotels/search.html')

    def post(self, request):
        Searchterm = request.POST.get("searchterm").title()

        if not Searchterm:
            hotels_list = Hotels.objects.all()
        elif Searchterm:
            hotels_list = Hotels.objects.filter(Q(city__icontains=Searchterm) | Q(address__icontains=Searchterm) | Q(name__icontains=Searchterm))

        Range = request.POST.get("daterange")
        Rangesplit = Range.split(' to ')
        Checkin = Rangesplit[0]
        Checkout = Rangesplit[1]
        request.session['checkin'] = Checkin
        request.session['checkout'] = Checkout


        context = {
            'hotels': hotels_list,
        }

        return render(request, 'hotels/hotel_list.html', context)


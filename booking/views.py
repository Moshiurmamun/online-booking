from django.shortcuts import render
from . import models
from hotels.models import Hotels, Room
import datetime

# how long the user is staying in a hotel & the total cost.
def bookroom(request, hotelid, roomid):

    FirstDate = request.session['checkin']
    SecDate = request.session['checkout']

    checkin = datetime.datetime.strptime(FirstDate, "%Y-%m-%d").date()
    checkout = datetime.datetime.strptime(SecDate, "%Y-%m-%d").date()

    timedeltaSum = checkout - checkin

    stayduration = timedeltaSum.days

    hotel = Hotels.objects.get(slug=hotelid)
    theroom = Room.objects.get(slug=roomid)

    price = theroom.price

    totalcost = stayduration * price

    context = {
        'checkin': checkin,
        'checkout': checkout,
        'stayduration': stayduration,
        'hotel': hotel,
        'theroom': theroom,
        'price':price,
        'totalcost':totalcost,
    }
    return render(request, 'booking/booking.html', context)


""""
def mybooking(request):
    booking = Booking.objects.filter(user=request.user)
    context = {
        'booking': booking,
    }
    return render(request, 'booking/mybooking.html', context)

"""

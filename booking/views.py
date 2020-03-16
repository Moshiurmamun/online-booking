import datetime

from django.shortcuts import render
from django import forms
from . import models
from hotels.models import Hotels, Room
import datetime
from .models import Booking
from django.urls import reverse
from django.http import HttpResponseRedirect




# ========================= Bookroom ========================
# how long the user is staying in a hotel & the total cost.
def bookroom(request, hotelid, roomid):

    FirstDate = request.session['checkin']
    SecDate = request.session['checkout']

    checkin = datetime.datetime.strptime(FirstDate, "%Y-%m-%d").date()
    checkout = datetime.datetime.strptime(SecDate, "%Y-%m-%d").date()

    timedeltaSum = checkout - checkin

    stayduration = timedeltaSum.days

    hotel = Hotels.objects.get(id=hotelid)
    theroom = Room.objects.get(id=roomid)

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



# ============================ storeBooking =========================
""""
def storeBooking(request, hotelid, roomid, checkin, checkout, totalcost):
    if request.method == 'POST':

        user = request.user
        hotel = Hotels.objects.get(id=hotelid)
        room = Room.objects.get(id=roomid)
        cost = totalcost
        newbooking = Booking()
        newbooking.hotel = hotel
        newbooking.room = room
        newbooking.user = user
        newbooking.checkin = checkin
        newbooking.checkout = checkout
        newbooking.totalcost = cost
        newbooking.save()


        del request.session['checkin']
        del request.session['checkout']
        link = reverse('hotels:userdash')
        return HttpResponseRedirect(link)
    else:
        url = reverse('hotels:userdash')
        return url


"""










""""
def mybooking(request):
    booking = Booking.objects.filter(user=request.user)
    context = {
        'booking': booking,
    }
    return render(request, 'booking/mybooking.html', context)
"""

import datetime
import os

from django.shortcuts import render
from django.http import HttpResponse
from django import forms
from . import models
from hotels.models import Hotels, Room
from .models import Booking
from django.urls import reverse
from django.http import HttpResponseRedirect

from django.views import View
from django.template.loader import get_template
from .utils import render_to_pdf



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
# ========================== selected number of rooms =====================
    if request.method=="POST":
        room_no=request.POST.get(roomid)


    totalcost = stayduration * price * float(room_no)
    totalcost = int(totalcost)
    context = {

        'checkin': checkin,
        'checkout': checkout,
        'stayduration': stayduration,
        'hotel': hotel,
        'theroom': theroom,
        'price':price,
        'r':room_no,
        'totalcost': totalcost,
    }
    return render(request, 'booking/booking.html', context)



# ============================ storeBooking ========================

def generate_random():
    uuid = os.urandom(7).hex()
    return uuid

def storeBooking(request, hotelid,checkin, checkout, roomid, totalcost):

    if request.method == 'POST':
        user = request.user
        hotel = Hotels.objects.get(id=hotelid)
        room = Room.objects.get(id=roomid)
        cost = totalcost
        newbooking = Booking()
        newbooking.hotel = hotel
        newbooking.room = room
        newbooking.invoice = generate_random()

        newbooking.user = user
        newbooking.checkin = checkin
        newbooking.checkout = checkout

        newbooking.totalcost = cost
        newbooking.save()

        # delete the session variables
        del request.session['checkin']
        del request.session['checkout']
        link = reverse('hotels:userdash')
        return HttpResponseRedirect(link)
    else:
        url = reverse('hotels:userdash')
        return url




# ========================= Booking view =======================
def mybooking(request):
    booking = Booking.objects.filter(user=request.user)
    context = {
        'booking': booking,
    }
    return render(request, 'booking/mybooking.html', context)



# ============================ Generate pdf =======================
## Generates a PDF using the render help function and outputs it as invoice.html
class GeneratePDF(View):
    def get(self, request, *args, **kwargs):
        booking = Booking.objects.get(id=self.kwargs['id'])
        template = get_template('invoice.html')
        context = {
            "booking": booking,
        }
        html = template.render(context)
        pdf = render_to_pdf('invoice.html', context)
        return HttpResponse(pdf, content_type='application/pdf')



def cancelbooking(request, id):
    booking = Booking.objects.get(id=id)
    booking.delete()
    link = reverse('booking:viewbookings')
    return HttpResponseRedirect(link)

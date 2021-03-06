import datetime
import os

from django.shortcuts import render
from django.http import HttpResponse
from django import forms
from . import models
from hotels.models import Hotels, Room
from .models import Booking, Notification
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
    discount = theroom.discount
    vat = theroom.vat
    service_charge = theroom.service_charge


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


# call jay na?
# ============================ storeBooking ========================

def generate_random():
    uuid = os.urandom(7).hex()
    return uuid

def storeBooking(request, hotelid,checkin, checkout, roomid, totalcost,room_no ):

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
        newbooking.room_booked=room_no
        newbooking.save()


        recv = hotel.user

        message = 'New request for '+str(room)+'.'
        Notification.objects.create(receiver=recv, message=message)


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




# ========================== Agent Notifications =========================
def notifications(request, p_id):
    notifications = Notification.objects.filter(receiver=request.user).order_by('-created')
    unread_notification = Notification.objects.filter(receiver=request.user, is_read=False).count()

    context = {
        'notifications': notifications,
        'count': unread_notification,
    }
    return render(request, 'booking/notifications.html', context)




def markAsRead(request):
    if request.user.is_authenticated:
        if request.GET.get('notification_id'):
            notification_id = request.GET.get('notification_id')
            notification_obj = Notification.objects.get(id=notification_id)

            if notification_obj in Notification.objects.all():
                notification_obj.is_read = True
                notification_obj.save()




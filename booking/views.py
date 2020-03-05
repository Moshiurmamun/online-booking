from django.shortcuts import render
from . import models
from hotels.models import Hotels, Room
import datetime



def bookroom(request, hotelid, roomid):

    #FirstDate = request.session['checkin']
    #SecDate = request.session['checkout']

    #checkin = datetime.datetime.strptime(FirstDate, "%Y-%m-%d").date()
    #checkout = datetime.datetime.strptime(SecDate, "%Y-%m-%d").date()

   # timedeltaSum = checkout - checkin

   # stayduration = timedeltaSum.days

    hotel = Hotels.objects.get(id=hotelid)
    theroom = Room.objects.get(id=roomid)

    #price = theroom.price
    #totalcost = stayduration * price

    context = {
        #'checkin': checkin,
        #'checkout': checkout,
       # 'stayduration': stayduration,
        'hotel': hotel,
        'theroom': theroom,
        #'price':price,
        #'totalcost':totalcost,
    }
    return render(request, 'booking/booking.html', context)


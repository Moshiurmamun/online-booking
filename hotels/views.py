from django.shortcuts import render, get_object_or_404, redirect
from .models import Places, Hotels, Room
from . import forms
from django.views import generic
from django.views import View
from django.db.models import Q
from booking.models import Booking
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from hotels.forms import HotelsAddForm

""""
def userdash(request):
    return render(request, 'hotels/userdash.html')
"""

# ============================= Place List like dhaka, coxsbazar etc....
def place_list(request):
    places = Places.objects.all()

###### Search
    Searchterm = request.POST.get("searchterm")

    if not Searchterm:
        hotels_list = Hotels.objects.all()
    elif Searchterm:
        hotels_list = Hotels.objects.filter(Q(city__icontains=Searchterm) | Q(address__icontains=Searchterm) | Q(name__icontains=Searchterm) | Q(description__icontains=Searchterm))

        Range = request.POST.get("daterange")
        Rangesplit = Range.split(' to ')
        Checkin = Rangesplit[0]
        Checkout = Rangesplit[1]
        request.session['checkin'] = Checkin
        request.session['checkout'] = Checkout

        context = {'object_list': hotels_list}
        return render(request, 'hotels/hotel_list.html', context)

    context = {
        'places': places,
        'hotels': hotels_list,
    }
    return render(request, 'hotels/list.html', context )



# ================ Hotels List ===================
def hotels_list(request, slug):
    #instance = get_object_or_404(Places, id=id)
    instance = Places.objects.get(slug=slug)
    hotels = Hotels.objects.active().filter(places=instance)


    paginator = Paginator(hotels,2)
    page = request.GET.get('page')
    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        queryset = paginator.page(1)
    except EmptyPage:
        queryset = paginator.page(paginator.num_pages)

########Search
    Searchterm = request.POST.get("searchterm")

    if not Searchterm:
        hotels_list = Hotels.objects.all()
    elif Searchterm:
        hotels_list = Hotels.objects.filter(Q(city__icontains=Searchterm) | Q(address__icontains=Searchterm) | Q(name__icontains=Searchterm) | Q(description__icontains=Searchterm))

        Range = request.POST.get("daterange")
        Rangesplit = Range.split(' to ')
        Checkin = Rangesplit[0]
        Checkout = Rangesplit[1]
        request.session['checkin'] = Checkin
        request.session['checkout'] = Checkout

        context = {'object_list': hotels_list}
        return render(request, 'hotels/hotel_list.html', context)

    context = {
        'object_list': queryset,
        'instance': instance,
    }

    return render(request, 'hotels/hotel_list.html', context)


# ========================= Rooms List ========================


def room_list(request, slug):

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

    thehotel = Hotels.objects.get(slug=slug)
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


    total_room=[]
    for r in rooms:
        data = [r.id,r.quantity]
        total_room.append(data)


    context = {
        'total_room':total_room,
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
            hotels_list = Hotels.objects.filter(Q(city__icontains=Searchterm) | Q(address__icontains=Searchterm) | Q(name__icontains=Searchterm) | Q(description__icontains=Searchterm))

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

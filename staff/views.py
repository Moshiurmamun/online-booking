from django.shortcuts import render, redirect
from booking.models import Booking
from hotels.models import Hotels, Places, Room
from hotels.forms import PlacesForm, HotelsAddForm, RoomAddForm


### Home view for staff
def staff_home(request):
    if request.user.is_staff or request.user.is_superuser:
        booking_list = Booking.objects.all()

        context = {
            'booking_list': booking_list,
        }

        return render(request, 'staff/staff_home.html', context)


### Places List
def places_list(request):
    if request.user.is_staff or request.user.is_superuser:
        places_list = Places.objects.all()


        context = {
            'places_list': places_list,
        }

        return render(request, 'staff/places.html', context)


### Add Places View
def add_places(request):
    if request.user.is_staff or request.user.is_superuser:
        if request.method == 'POST':
            form = PlacesForm(request.POST or None, request.FILES or None)
            if form.is_valid():
                form.save()

                return redirect('staff:places_list')
        else:
            form = PlacesForm()

        context = {
            'form': form,
        }
        return render(request, 'staff/add_places.html', context)




### Hotels View
def hotels(request):
    if request.user.is_staff or request.user.is_superuser:
        places_list = Places.objects.all()
        hotels_list = Hotels.objects.all()

        context  = {
            'places':places_list,
            'hotels': hotels_list,
        }

        return render(request, 'staff/hotels.html', context)


### Add Hotel View
def addhotel(request, place_id):
    if request.user.is_staff or request.user.is_superuser:
        places = Places.objects.get(id=place_id)

        if request.method == 'POST':
            form = HotelsAddForm(request.POST or None, request.FILES or None)

            if form.is_valid():
                instance = form.save(commit=False)
                instance.places = places
                instance.save()
                return redirect('staff:hotels')

        else:
            form = HotelsAddForm()

        context = {
            'form': form,
        }
        return render(request, 'staff/add_hotel.html', context)


### Room View
def rooms(request):
    if request.user.is_staff or request.user.is_superuser:
        places_list = Places.objects.all()
        hotels_list = Hotels.objects.all()
        rooms_list = Room.objects.all()

        context = {
            'places': places_list,
            'hotels': hotels_list,
            'rooms': rooms_list,
        }

        return render(request, 'staff/rooms.html', context)


### Add Room
def add_room(request, id):
    if request.user.is_staff or request.user.is_superuser:
        hotel = Hotels.objects.get(id=id)

        if request.method == 'POST':
            form = RoomAddForm(request.POST or None, request.FILES or None)

            if form.is_valid():
                instance = form.save(commit=False)
                instance.hotel = hotel
                instance.save()
                return redirect('staff:rooms')
        else:
            form = RoomAddForm()

        context = {
            'form': form
        }
        return render(request, 'staff/add_room.html', context)





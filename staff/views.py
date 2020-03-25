from django.shortcuts import render, redirect, get_object_or_404
from booking.models import Booking
from hotels.models import Hotels, Places, Room
from hotels.forms import PlacesForm, HotelsAddFormAdmin, RoomAddForm
from booking.models import Booking
from contact.models import Contact
from contact.forms import ReplyMessage
from django.http import JsonResponse



### Home view for staff
def staff_home(request):
    if request.user.is_superuser:
        booking_list = Booking.objects.all()


        context = {
            'booking_list': booking_list,

        }

        return render(request, 'staff/staff_home.html', context)


### View Booking
def view_booking(request):
    #if request.user.is_superuser:


    return render(request, 'staff/view_booking.html')



### Places List
def places_list(request):
    if request.user.is_superuser:
        places_list = Places.objects.all()


        context = {
            'places': places_list,
        }

        return render(request, 'staff/places.html', context)


### Add Places View
def add_places(request):
    if request.user.is_superuser:
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



### Edit Places View
def edit_places(request, id):
    if request.user.is_superuser:
        instance = get_object_or_404(Places, id=id)

        form = PlacesForm(request.POST or None, request.FILES or None, instance=instance)
        if form.is_valid():
            form.save()

        context = {
            'form': form,
        }
        return render(request, 'staff/add_places.html', context)


### Hotels View
def hotels(request, p_id):
    if request.user.is_superuser:
        instance = Places.objects.get(id=p_id)
        hotels_list = Hotels.objects.all().filter(places=instance)

        context  = {
            'places':places_list,
            'hotels': hotels_list,
        }

        return render(request, 'staff/hotels.html', context)


### Add Hotel View
def addhotel(request, place_id):
    if request.user.is_superuser:
        places = Places.objects.get(id=place_id)

        if request.method == 'POST':
            form = HotelsAddFormAdmin(request.POST or None, request.FILES or None)

            if form.is_valid():
                instance = form.save(commit=False)
                instance.places = places
                instance.save()
                return redirect('staff:hotels')

        else:
            form = HotelsAddFormAdmin()

        context = {
            'form': form,
        }
        return render(request, 'staff/add_hotel.html', context)



### Edit Hotel view
def edit_hotel(request, id):
    if request.user.is_superuser:
        instance = get_object_or_404(Hotels, id=id)

        form = HotelsAddFormAdmin(request.POST or None, request.FILES or None, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('staff:hotels')

        context = {
            'form': form,
        }
        return render(request, 'staff/add_hotel.html', context)



### Room View
def rooms(request, h_id):
    if request.user.is_superuser:
        thehotel = Hotels.objects.get(id=h_id)
        rooms = Room.objects.filter(hotel=thehotel)

        context = {
            'hotels': thehotel,
            'rooms': rooms,
        }

        return render(request, 'staff/rooms.html', context)


### Add Room
def add_room(request, id):
    if request.user.is_superuser:
        hotel = Hotels.objects.get(id=id)

        if request.method == 'POST':
            form = RoomAddForm(request.POST or None, request.FILES or None)

            if form.is_valid():
                instance = form.save(commit=False)
                instance.hotel = hotel
                instance.save()
                return redirect('staff:staff_home')
        else:
            form = RoomAddForm()

        context = {
            'form': form
        }
        return render(request, 'staff/add_room.html', context)



### Edit Room
def edit_room(request, id):
    if request.user.is_superuser:
        instance = get_object_or_404(Room, id=id)

        form = RoomAddForm(request.POST or None, request.FILES or None, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('/')

        context = {
            'form': form,
        }
        return render(request, 'staff/add_room.html', context)





# ===================================== Staff Message View ===============================
# admin je gular reply dibe segula True hoye jabe mane ekhane show korbe na
# jegula unreplied segulai show korbe
def queries(request):
    if request.user.is_superuser:
        message_list = Contact.objects.filter(replied=False).order_by('-msg_send_date')

        context = {
            'messages': message_list,
        }
        return render(request, 'staff/messages.html', context)
    else:
        return render(request, 'staff/page_not_found.html')




# ================== staff reply message ==================
def replyMessage(request, id):
    if request.user.is_superuser:
        instance = get_object_or_404(Contact, id=id)

        if request.method == 'POST':
            form = ReplyMessage(request.POST or None, instance=instance)
            if form.is_valid():
                instance = form.save(commit=False)
                instance.replied =True
                instance.save()
                return redirect('staff:queries')
        else:
            form = ReplyMessage()

        context = {
            'form': form,
            'instance': instance,
        }
        return render(request, 'contact/reply.html', context)

    else:
        return render(request, 'staff/page_not_found.html')






# ================= replied message view ====================
def ApiRepliedMessage(request):
    if request.user.is_superuser:
        if request.GET.get('message_id'):
            message_id = request.GET.get('message_id')
            message_obj = Contact.objects.get(id=message_id)

            data = dict()
            if message_obj in Contact.objects.all():
                message_obj.replied = True
                message_obj.save()
                data['replied'] = 'success'
                message_list = Contact.objects.filter(replied=False).order_by('-msg_send_date')


                context = {
                    'messages': message_list
                }
            return JsonResponse(data)

        return JsonResponse({
            'replied': 'error'
        })

    else:
        return render(request, 'staff/page_not_found.html')


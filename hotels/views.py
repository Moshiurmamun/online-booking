from django.shortcuts import render
from . models import Hotels


def hotel_list(request):
    hotels_list = Hotels.objects.all()

    context = {
        'hotels_list': hotels_list,
    }
    return render(request, 'hotels/hotel_list.html', context)

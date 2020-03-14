from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.contrib.auth import login, logout
from booking.models import Booking
from .models import UserProfile
from . import forms
from django.contrib.auth.models import User
from accounts import models as account_model
from django.contrib.auth import update_session_auth_hash
from hotels.forms import HotelsAddForm,RoomAddForm
from hotels.models import Places,Hotels, Room


#register as user
class RegistrationUser(View):
    template_name = 'accounts/signup.html'

    def get(self, request):

        form = forms.UserRegistrationForm()

        variables = {
            'form': form,
        }

        return render(request, self.template_name, variables)

    def post(self, request):

        form = forms.UserRegistrationForm(request.POST or None)

        if form.is_valid():
            form.deploy()
            return redirect('accounts:login')

        variables = {
            'form': form,
        }

        return render(request, self.template_name, variables)



#logout functionality
def logout_request(request):
    logout(request)
    return redirect('accounts:login')



#login
class Login(View):
    template_name = 'accounts/login.html'

    def get(self, request):
        form = forms.Login()

        variables = {
            'form': form,
        }

        return render(request, self.template_name, variables)

    def post(self, request):
        form = forms.Login(request.POST or None)

        if form.is_valid():
            user = form.login_request()
            if user:
                login(request, user)

                return redirect('home')

        variables = {
            'form': form,
        }

        return render(request, self.template_name, variables)




class ClientPermissionMixin(object):
    def has_permissions(self, request):
        return request.user.is_authenticated== True

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            if not self.has_permissions(request):
                return redirect('accounts:login')
            return super(ClientPermissionMixin, self).dispatch(
                request, *args, **kwargs)
        else:
            return redirect('accounts:login')


#change basic info
class ChangeBasicInfo(ClientPermissionMixin, View):
    template_name = 'accounts/change-basic-info.html'

    def get(self, request):

        form = forms.BasicInfoChangeForm(instance=request.user)

        variables = {
            'form': form,
        }

        return render(request, self.template_name, variables)

    def post(self, request):

        form = forms.BasicInfoChangeForm(request.POST or None,request.FILES or None, instance=request.user)

        if form.is_valid():
            form.save()
            return redirect('home')

        variables = {
            'form': form,
        }

        return render(request, self.template_name, variables)




#change password
class ChangePassword(ClientPermissionMixin, View):
    template_name = 'accounts/change-password.html'

    def get(self, request):

        form = forms.ChangePasswordForm(user=request.user)

        variables = {
            'form': form,
        }

        return render(request, self.template_name, variables)

    def post(self, request):

        form = forms.ChangePasswordForm(data=request.POST or None, user=request.user)

        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('home')

        variables = {
            'form': form,
        }

        return render(request, self.template_name, variables)



##### Profile
def profile(request, profile_id):
    user = get_object_or_404(account_model.UserProfile, id=profile_id)
    #userprofile = account_model.UserProfile.objects.get(user = user)
    hotels = Hotels.objects.filter(user=user)

    context = {
        'user': user,
        'hotels': hotels,
    }
    return render(request, 'accounts/profile.html', context)




###### list_property
def create_property(request, user_id):
    # print(property_id)
    # places = Places.objects.get(id=property_id)
    if request.method == 'POST':
        form = HotelsAddForm(request.POST or None, request.FILES or None)

        if form.is_valid():
            instance = form.save(commit=False)
            user = UserProfile.objects.get(id=user_id)
            instance.user=user
            instance.save()
            return redirect('home')
    else:
        form = HotelsAddForm()

    context = {
        'form': form,

    }

    return render(request, 'accounts/list_property.html', context)



#### Add Room
def add_room(request, id):

    if request.method == 'POST':
        form = RoomAddForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            instance = form.save(commit=False)
            user = UserProfile.objects.get(id=id)
            instance.user = user
            instance.save()
            return redirect('home')
    else:
        form = RoomAddForm()

    context = {
        'form': form,
    }
    return render(request, 'accounts/create_rooms.html', context)


#### View All Room
def view_all_rooms(request, id):
    user = get_object_or_404(account_model.UserProfile, id=id)

    rooms = Room.objects.filter(user=user)
    print(rooms)

    context = {
        'rooms': rooms,
    }
    return render(request, 'accounts/view_all_rooms.html', context)

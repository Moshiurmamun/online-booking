import requests
import json
import os


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


from . import models

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



# =====================logout functionality===================
def logout_request(request):
    logout(request)
    return redirect('accounts:login')



#=======================login ==================================
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


# =====================change basic info=====================
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




#=======================change password==========================
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



#====================== Profile =======================
def profile(request, profile_id):
    user = get_object_or_404(account_model.UserProfile, id=profile_id)
    #userprofile = account_model.UserProfile.objects.get(user = user)
    hotels = Hotels.objects.filter(user=user)

    context = {
        'user': user,
        'hotels': hotels,
    }
    return render(request, 'accounts/profile.html', context)




# ====================== Client create list_property ======================
def create_property(request, user_id):
    # print(property_id)
    # places = Places.objects.get(id=property_id)
    if request.method == 'POST':
        form = HotelsAddForm(request.POST or None, request.FILES or None)

        if form.is_valid():
            instance = form.save(commit=False)
            user = UserProfile.objects.get(email=request.user)
            instance.user=user
            instance.save()
            return redirect('home')
    else:
        form = HotelsAddForm()

    context = {
        'form': form,

    }

    return render(request, 'accounts/list_property.html', context)



# ========================= Edit Property ========================

def edit_property(request, hotel_id):

        instance = get_object_or_404(Hotels, id=hotel_id)

        form = HotelsAddForm(request.POST or None, request.FILES or None,instance=instance)


        if form.is_valid():
            form.save()
            return redirect('/')

        context = {
            'form': form,
        }
        return render(request, 'accounts/edit_property.html', context)









# ==================================== View All Room =========================== #
def view_all_rooms(request):
    user = UserProfile.objects.get(email=request.user)

    rooms = Room.objects.filter(user=user)

    context = {
        'rooms': rooms,
    }
    return render(request, 'accounts/view_all_rooms.html', context)



# ========================================== Add Room ================================
def add_room(request):
    if request.method == 'POST':
        form = RoomAddForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            instance = form.save(commit=False)
            user = UserProfile.objects.get(email=request.user)
            instance.user = user
            instance.save()
            return redirect('home')
    else:
        form = RoomAddForm()

    context = {
        'form': form,
    }
    return render(request, 'accounts/create_rooms.html', context)


# ============================= Edit Room ==================================
def edit_room(request, room_id):

    instance = get_object_or_404(Room, id=room_id)
    form = RoomAddForm(request.POST or None, request.FILES or None, instance=instance)

    if form.is_valid():
        form.save()
        return redirect('/')
    context = {
        'form': form,
    }

    return render(request, 'accounts/edit_room.html', context)






# =============================================== Facebook Login ====================================== #
def validate_access_token(access_token):
    url = ' https://graph.facebook.com/me?access_token={}'.format(access_token)

    r = requests.get(url)

    response_data = r.content.decode('utf-8')

    data = json.loads(response_data)

    try:
        if data['error']:
            return False
    except:
        return True

def get_uuid():
    return os.urandom(2).hex()


class SocialSigninApi(APIView):
    def post(self, request, uid):
        try:
            get_user = models.SocialAuth.objects.get(uid=uid)
            access_token = request.POST.get('access_token')

            validate_acss_token = validate_access_token(access_token)

            if validate_acss_token:
                get_user.access_token = access_token
                get_user.save()

                user_authenticate = models.SocialAuthModelBackend.authenticate(self, request, uid)

                login(request, user_authenticate, backend='django.contrib.auth.backends.ModelBackend')

                return Response({
                    'status': status.HTTP_200_OK,
                    'sign_up': "old"
                })
            else:
                return Response({
                    'status': status.HTTP_400_BAD_REQUEST
                })

        except:

            access_token = request.POST.get('access_token')
            user_name = request.POST.get('user_name').lower()
            user_email = request.POST.get('user_email')

            validate_acss_token = validate_access_token(access_token)

            if validate_acss_token:
                password = get_uuid()

                create_user = models.UserProfile(firstname=user_name, email=user_email)
                create_user.set_password(password)
                create_user.save()

                social_auth = models.SocialAuth(user=create_user, uid=uid, access_token=access_token)
                social_auth.save()

                user_authenticate = models.SocialAuthModelBackend.authenticate(self, request, uid)

                login(request, user_authenticate, backend='django.contrib.auth.backends.ModelBackend')

                return Response({
                    'status': status.HTTP_200_OK,
                    'sign_up': "new"
                })
            else:
                return Response({
                    'status': status.HTTP_400_BAD_REQUEST
                })

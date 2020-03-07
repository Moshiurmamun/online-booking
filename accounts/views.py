from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import login, logout
from booking.models import Booking
from . import models
from . import forms


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




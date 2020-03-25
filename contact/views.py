from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from .models import Contact
from .forms import *
from accounts.models import UserProfile
from accounts import models as account_model



def contactUs(request):
    if request.method == 'POST':
        form = ContactForm(request.POST or None)
        if form.is_valid():
            if request.user.is_authenticated:
                instance = form.save(commit=False)
                instance.user = request.user
                instance.save()
                return redirect('accounts:messages', request.user)
            else:
                form.save()
                return redirect('home')

    else:
        form = ContactForm()

    context = {
        'form': form,
    }

    return render(request, 'contact/contact_form.html', context)





def messages(request, id):
    user = get_object_or_404(account_model.UserProfile, id=id)
    messages = Contact.objects.filter(user=user).order_by('id')

    if request.method == 'POST':
        form = SendMessage(request.POST or None)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.name = request.user.firstname
            instance.save()
            return redirect('/')
    else:
        form = SendMessage()

    context = {
        'messages': messages,
        'form': form,
    }
    return render(request, 'contact/my_messages.html', context)

from django import forms
import re
from django.contrib.auth import authenticate
from accounts import models as account_model
from django.contrib.auth.forms import PasswordChangeForm
from . import models


class UserRegistrationForm(forms.Form):
    firstname = forms.CharField(max_length=255, required=False, widget=forms.TextInput(attrs={'placeholder': 'First name', 'class':'form-control'}))
    lastname = forms.CharField(max_length=255, required=False, widget=forms.TextInput(attrs={'placeholder': 'Last name', 'class':'form-control'}))
    email = forms.CharField(max_length=255, required=False, widget=forms.TextInput(attrs={'placeholder': 'youremail@something.com', 'class':'form-control'}))
    phone = forms.CharField(max_length=255, required=False, widget=forms.TextInput(attrs={'placeholder': '01974265888', 'class':'form-control'}))
    password1 = forms.CharField(max_length=20, required=False, widget=forms.PasswordInput(attrs={'placeholder': 'Password', 'class':'form-control'}))
    password2 = forms.CharField(max_length=20, required=False, widget=forms.PasswordInput(attrs={'placeholder': 'Retype', 'class':'form-control'}))




    def clean(self):
        firstname = self.cleaned_data.get('firstname')
        lastname = self.cleaned_data.get('lastname')
        email = self.cleaned_data.get('email')
        phone = self.cleaned_data.get('phone')
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if len(email) < 1:
            raise forms.ValidationError('Enter email address!')
        else:
            email_correction = re.match('^[_a-zA-Z0-9-]+(\.[_a-zA-Z0-9-]+)*@[a-zA-Z0-9-]+(\.[a-zA-Z0-9-]+)*(\.[a-zA-Z]{2,4})$', email)

            if not email_correction:
                raise forms.ValidationError('Email not correct!')
            else:
                email_exist = models.UserProfile.objects.filter(email__iexact=email).exists()

                if email_exist:
                    raise forms.ValidationError('Already registered using this email! Try to login!')
                else:
                    if len(phone) < 1:
                        raise forms.ValidationError('Enter phone number!')
                    else:
                        if len(password1) < 8:
                            raise forms.ValidationError("Password is too short!")
                        else:
                            if password1 != password2:
                                raise forms.ValidationError("Password not matched!")



    def deploy(self):
        firstname = self.cleaned_data.get('firstname')
        lastname = self.cleaned_data.get('lastname')
        email = self.cleaned_data.get('email')
        phone = self.cleaned_data.get('phone')
        password1 = self.cleaned_data.get('password1')

        user = models.UserProfile(firstname=firstname, lastname=lastname, email=email, phone=phone)
        user.set_password(password1)
        user.save()

#login
class Login(forms.Form):
    email = forms.CharField(max_length=255, required=False, widget=forms.TextInput(attrs={'placeholder': 'youremail@something.com',  'class':'form-control'}))
    password = forms.CharField(max_length=20, required=False, widget=forms.PasswordInput(attrs={'placeholder': 'Password', 'class':'form-control'}))


    def clean(self):
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')

        if len(email) < 1:
            raise forms.ValidationError('Enter email address!')
        else:
            email_correction = re.match('^[_a-zA-Z0-9-]+(\.[_a-zA-Z0-9-]+)*@[a-zA-Z0-9-]+(\.[a-zA-Z0-9-]+)*(\.[a-zA-Z]{2,4})$', email)

            if not email_correction:
                raise forms.ValidationError('Email not correct!')
            else:
                if len(password) < 8:
                    raise forms.ValidationError("Password is too short!")
                else:
                    user = authenticate(email=email, password=password)

                    if not user:
                        raise forms.ValidationError("Invalid email or password. Please try again!")
                    else:
                        if not user.is_active:
                            raise forms.ValidationError("This account is no longer active, please contact customer support!")





    def login_request(self):
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')
        user = authenticate(email=email, password=password)
        return user







class BasicInfoChangeForm(forms.ModelForm):

    class Meta:
        model = account_model.UserProfile
        fields = [
            'firstname',
            'lastname',
            'email',
            'phone',
            'image',
            'address',
            'country',

        ]


#change password form
class ChangePasswordForm(PasswordChangeForm):
    old_password = forms.CharField(label='Old Password', max_length=20, required=False, widget=forms.PasswordInput(attrs={'placeholder': 'Old password'}))
    new_password1 = forms.CharField(label='New Password', max_length=20, required=False, widget=forms.PasswordInput(attrs={'placeholder': 'New password'}))
    new_password2 = forms.CharField(label='Confirm Password', max_length=20, required=False, widget=forms.PasswordInput(attrs={'placeholder': 'Retype'}))

    def clean(self):
        old_password = self.cleaned_data.get('old_password')
        new_password1 = self.cleaned_data.get('new_password1')
        new_password2 = self.cleaned_data.get('new_password2')

        if len(new_password1) < 8:
            raise forms.ValidationError("Password is too short!")
        else:
            if new_password1 != new_password2:
                raise forms.ValidationError("Password not matched!")

from django import forms
from .models import UserProfile
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
import re


class SignupForm(forms.Form):
	username  = forms.CharField(max_length=12, required=False, widget=forms.TextInput(
				attrs={'class':'form-control',}))

	email 	  = forms.EmailField(required=False, widget=forms.TextInput(
				attrs={'class':'form-control',}))

	phone 	= forms.CharField(max_length= 11, required=False, widget=forms.TextInput(
						attrs={'class': 'form-control', 'placeholder': "Mobile"}))

	password1 = forms.CharField(max_length=20, required=False, widget=forms.PasswordInput(
				attrs={'class':'form-control',}))

	password2 = forms.CharField(max_length=20, required=False, widget=forms.PasswordInput(
				attrs={'class':'form-control',}))



	def clean(self):
		username  = self.cleaned_data.get('username')
		email 	  = self.cleaned_data.get('email')
		password1 = self.cleaned_data.get('password1')
		password2 = self.cleaned_data.get('password2')

		if len(username) < 1:
			raise forms.ValidationError("Please enter a valid username.")
		else:
			user_exist = User.objects.filter(username__iexact=username).exists()

			if user_exist:
				raise forms.ValidationError("This username isn't available. Please try again.")
			else:
				if len(email) < 1:
					raise forms.ValidationError("Please enter a valid email address.")
				else:
					email_correction = re.match('[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})', email)

					if email_correction == None:
						raise forms.ValidationError('Please enter a valid email address.')
					else:
						email_exist = User.objects.filter(email__iexact=email).exists()
						if email_exist:
							raise forms.ValidationError("This email is taken by another account.")
						else:
							if len(password1) < 8:
								raise forms.ValidationError("Password is too short!")
							else:
								if password1 != password2:
									raise forms.ValidationError("Password not match!")

	def signup(self,request):
		username  = self.cleaned_data.get('username')
		email 	  = self.cleaned_data.get('email')
		password1 = self.cleaned_data.get('password1')

		user = User.objects.create_user(username=username, email=email)
		user.set_password(password1)

		return user



# --------------------------------------
# -------------Login Form--------------
# --------------------------------------
class LoginForm(forms.Form):
	username 	= forms.CharField(max_length=255, required=False, widget=forms.TextInput(
		attrs={'class':'form-control',}))

	password	= forms.CharField(max_length=20, required=False, widget=forms.PasswordInput(
		attrs={'class':'form-control',}))


	def clean(self):
		username = self.cleaned_data.get('username')
		password = self.cleaned_data.get('password')

		if len(username) < 1:
			raise forms.ValidationError("The username and password you entered didn't match. Please check and try agian.")
		else:
			if len(password) < 8:
				raise forms.ValidationError("The username and password you entered didn't match. Please check and try agian.")
			else:
				user = authenticate(username=username, password=password)

				if not user or not user.is_active:
					raise forms.ValidationError("The username and password you entered didn't match. Please check and try agian.")
		return self.cleaned_data

	def login(self, request):
		username = self.cleaned_data.get('username')
		password = self.cleaned_data.get('password')

		user = authenticate(username=username, password=password)

		return user


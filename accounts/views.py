from . forms import SignupForm, LoginForm
from . models import UserProfile
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout



def signup_views(request):
	if request.method == 'POST':
		form = SignupForm(request.POST)

		if form.is_valid():
			user = form.signup(request)
			user.save()
			return redirect('accounts:login')

	else:
		form = SignupForm()

	context = {
		'form': form,
	}

	return render(request, 'accounts/signup.html', context)


# --------------------------------------
# ------------Login Views--------------
# --------------------------------------
def login_views(request):
	if request.method == 'POST':
		form = LoginForm(data=request.POST)
		if form.is_valid():
			user = form.login(request)
			if user:
				login(request,user)
				return redirect('home')
	else:
		form = LoginForm()

	context = {
		'form': form,
	}

	return render(request, 'accounts/login.html', context)



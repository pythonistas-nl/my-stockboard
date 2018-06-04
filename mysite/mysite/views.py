from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout

from .forms import LoginForm, RegisterForm

from bs4 import BeautifulSoup
import requests
import json

def home(request):
	template = loader.get_template('stock_data/home.html')
	context = {
	}
	print(request.user)
	return HttpResponse(template.render(context, request))

def login_member(request):
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		form = LoginForm(data=request.POST)
		# print("form: " + str(form))
		# print("request.POST: " + str(request.POST))
		#print(form.error)
		#print(form.is_bound)
		if form.is_valid():
			# process the data in form.cleaned_data as required
			# ...
			user = authenticate(request, username=username, password=password)
			print("in VALID")
			if user is not None:
				print("init")
				login(request, user)
				# A backend authenticated the credentials
			else:
				print("WOW")
				# No backend authenticated the credentials
			# redirect to a new URL:
			return HttpResponseRedirect('/stocks/')

	# if a GET (or any other method) we'll create a blank form
	else:
		form = LoginForm()
	return render(request, 'stock_data/login.html', {'form': form})

def register(request):
	if request.method == 'POST':
		form = RegisterForm(request.POST)
		print("form: " + str(form))
		print("request.POST: " + str(request.POST))
		if form.is_valid():
			# process the data in form.cleaned_data as required
			# ...
			form.save()
			# redirect to a new URL:
			return HttpResponseRedirect('/login/')

	# if a GET (or any other method) we'll create a blank form
	else:
		form = RegisterForm()
	return render(request, 'stock_data/register.html', {'form': form})

def logout_member(request):
	logout(request)
	return render(request, 'stock_data/logout.html')



#render(request, 'mysite/home.html')
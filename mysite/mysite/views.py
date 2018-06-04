from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.shortcuts import render
from django.contrib.auth import authenticate

from .forms import LoginForm, RegisterForm


from bs4 import BeautifulSoup
import requests
import json

def home(request):
	template = loader.get_template('stock_data/home.html')
	context = {
	}

	return HttpResponse(template.render(context, request))

def login(request):
	if request.method == 'POST':
		form = LoginForm(request.POST)
		if form.is_valid():
			# process the data in form.cleaned_data as required
			# ...
			user = authenticate(username='john', password='secret')
			if user is not None:
				c=2+2
				# A backend authenticated the credentials
			else:
				c=2-2
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



#render(request, 'mysite/home.html')
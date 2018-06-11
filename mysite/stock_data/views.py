from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from .models import Stocks

from iexfinance import Stock as stock_pull
import requests
import json
import time

@login_required(login_url='/login/')
def index(request):
	# Check to see if the logged in user has any stocks they are following, via the Stocks model
	current_user = User.objects.get(username=request.user)
	try:
		model_stocks_list = Stocks.objects.get(user=current_user)
	# If user does not have any stocks, make a new instance for them in the Stocks model, but make it blank
	except Stocks.DoesNotExist:
		context = {}
		s = Stocks(user=current_user, stock_list = '')
		s.save()
		return render(request, 'stock_data/index.html', context)

	# If user had a stock watch list, convert that data into a list structure
	stocks_list = model_stocks_list.stock_list.split(', ')

	if request.method == 'POST':
		# If the user submits the form with a company name, we should add this to the stocks_list variable
		if stocks_list != ['']:
			stocks_list.append(request.POST['stock_symbol'])
		else:
			stocks_list = [request.POST['stock_symbol']]

		# Now, convert the list of stocks into a string again and save it into the model
		model_stocks_list.stock_list = ', '.join(stocks_list)
		model_stocks_list.save()

	# Using the IEXTrading module, pull the latest stock data from their API for each stock the user is following
	# Store this data in a context variable for the html generation
	ohlc_data_dict = {}
	for stock in stocks_list:
		get_stock_ohlc = stock_pull(stock).get_ohlc()
		ohlc_data_dict[stock] = [get_stock_ohlc["open"]["price"], get_stock_ohlc["high"], get_stock_ohlc["low"], get_stock_ohlc["close"]["price"]]
	context = {'ohlc_data': ohlc_data_dict}
	return render(request, 'stock_data/index.html', context)



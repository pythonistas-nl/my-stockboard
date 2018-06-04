from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from .models import Stocks


from bs4 import BeautifulSoup
import requests
import json

@login_required(login_url='/login/')
def index(request):
	def stock_ohlc(stock_symbol):
		api_key = "MQ6XW7KDB2DF9M5O"
		parameter_options = {"TIME_SERIES_INTRADAY": 
								{"function": "TIME_SERIES_INTRADAY", "symbol": stock_symbol, "interval": "1min", "apikey": api_key},
							"TIME_SERIES_DAILY": 
								{"function": "TIME_SERIES_DAILY", "symbol": stock_symbol, "apikey": api_key}}
		parameters = parameter_options["TIME_SERIES_DAILY"]
		response = requests.get('https://www.alphavantage.co/query?', params= parameters)
		json_data = json.loads(response.content)
		last_update_time = json_data["Meta Data"]["3. Last Refreshed"]
		last_update_data = json_data["Time Series (Daily)"][last_update_time]
		ohlc_data = last_update_data
		return ohlc_data

	if request.method == 'POST':
		# If the user submits the form with a company, we should add this company to their model and display it on this page
		pass
	else:
		### if the user just visits this page w/o submitting anything, then only show their stock's data
		

	#	stock_symbol = request.POST['stock_symbol'].upper()
		# start off by fetching all the stock interests this user has from the Stocks model
		current_user = User.objects.get(username=request.user)
		string_stocks_list = Stocks.objects.get(user=current_user)
		stocks_list = string_stocks_list.stock_list.split(', ')
		ohlc_data_dict = {}
		for stock in stocks_list:
			ohlc_data_dict[stock] = stock_ohlc(stock)
		context = {'ohlc_data': ohlc_data_dict}
		#print(context_2)

	return render(request, 'stock_data/index.html', context)

@login_required(login_url='/login/')
def data_fetching(request):
	api_key = "MQ6XW7KDB2DF9M5O"
	#stock_name = "Facebook"
	stock_symbol = request.POST['stock_symbol'].upper()
 
	parameter_options = {"TIME_SERIES_INTRADAY": 
							{"function": "TIME_SERIES_INTRADAY", "symbol": stock_symbol, "interval": "1min", "apikey": api_key},
						"TIME_SERIES_DAILY": 
							{"function": "TIME_SERIES_DAILY", "symbol": stock_symbol, "apikey": api_key}}
	parameters = parameter_options["TIME_SERIES_DAILY"]
	response = requests.get('https://www.alphavantage.co/query?', params= parameters)

	json_data = json.loads(response.content)
	last_update_time = json_data["Meta Data"]["3. Last Refreshed"]
	last_update_data = json_data["Time Series (Daily)"][last_update_time]
	ohlc_data = last_update_data
	return HttpResponseRedirect(reverse('stock_data:result'))

@login_required(login_url='/login/')
def result(request):
	

	template = loader.get_template('stock_data/stock_info.html')
	context = {
		'ohlc_data': ohlc_data,
		'stock_name': stock_name,
		'stock_symbol': stock_symbol
	}

	return HttpResponse(template.render(context, request))



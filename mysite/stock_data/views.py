from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.shortcuts import render


from bs4 import BeautifulSoup
import requests
import json

def index(request):
	return render(request, 'stock_data/index.html')

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

def result(request):
	

	template = loader.get_template('stock_data/stock_info.html')
	context = {
        'ohlc_data': ohlc_data,
        'stock_name': stock_name,
        'stock_symbol': stock_symbol
    }

	return HttpResponse(template.render(context, request))



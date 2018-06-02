from django.http import HttpResponse
from django.template import loader

from bs4 import BeautifulSoup
import requests
import json

api_key = "MQ6XW7KDB2DF9M5O"

def index(request):
	# try:
	#     stock = input("What stock are you interested in? \n")
	# except:
	#     stock = raw_input("What stock are you interested in? \n")
	stock_name = "Facebook"
	stock_symbol = "FB"

	parameter_options = {"TIME_SERIES_INTRADAY": 
							{"function": "TIME_SERIES_INTRADAY", "symbol": stock_symbol.upper(), "interval": "1min", "apikey": api_key},
						"TIME_SERIES_DAILY": 
							{"function": "TIME_SERIES_DAILY", "symbol": stock_symbol.upper(), "apikey": api_key}}
	parameters = parameter_options["TIME_SERIES_DAILY"]
	response = requests.get('https://www.alphavantage.co/query?', params= parameters)

	json_data = json.loads(response.content)
	last_update_time = json_data["Meta Data"]["3. Last Refreshed"]
	last_update_data = json_data["Time Series (Daily)"][last_update_time]
	ohlc_data = last_update_data
	#total_volume

	markets_open_date = "2018-06-01" # 09:30:00"
	timestamp_data = "09:30:00"
	template = loader.get_template('stock_data/index.html')
	context = {
        'ohlc_data': ohlc_data,
        'stock_name': stock_name
    }

	return HttpResponse(template.render(context, request))
from bs4 import BeautifulSoup
import requests
import json

api_key = "MQ6XW7KDB2DF9M5O"

try:
    stock = input("What stock are you interested in? \n")
except:
    stock = raw_input("What stock are you interested in? \n")

parameters = {"function": "TIME_SERIES_INTRADAY", "symbol": stock.upper(), "interval": "1min", "apikey": api_key}
response = requests.get('https://www.alphavantage.co/query?', params= parameters)

json_data = json.loads(response.content)
last_update_time = json_data["Meta Data"]["3. Last Refreshed"]
last_update_data = json_data["Time Series (1min)"][last_update_time]
total_volume

markets_open_date = "2018-06-01" # 09:30:00"
timestamp_data = "09:30:00"





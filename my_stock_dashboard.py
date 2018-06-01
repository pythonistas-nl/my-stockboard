# import libraries
#import urllib2
from bs4 import BeautifulSoup
import requests
import json

# https://www.alphavantage.co/ API Key
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

#data = 'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=' + stock + '&interval=1min&apikey=' + api_key

#print(data)

#<span class="IsqQVc NprOob i4ncfvccpph4-zJFzKq8ukm8">1,607.97</span>

##response = requests.get(g_data)
##soup = BeautifulSoup(response.content, 'html.parser')
##posts = soup.find_all('tr', class_='athing comtr ')




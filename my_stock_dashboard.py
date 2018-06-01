# import libraries
#import urllib2
#from bs4 import BeautifulSoup

stock = input("What stock are you interested in? \n")

google_stock_data = 'https://www.google.com/search?q=' + stock + '+stock+price&pws=0&gl=us&gws_rd=cr'

print(google_stock_data)

#<span class="IsqQVc NprOob i4ncfvccpph4-zJFzKq8ukm8">1,607.97</span>


from django.db import models

class Stocks(models.Model):
	company_name = models.CharField(max_length=200)
	stock_symbol = models.CharField(max_length=20)
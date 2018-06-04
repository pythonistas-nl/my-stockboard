from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

class Stocks(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	stock_list = models.CharField(max_length=200)
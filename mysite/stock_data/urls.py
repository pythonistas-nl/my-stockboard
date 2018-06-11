from django.urls import path

from . import views

app_name = 'stock_data'
urlpatterns = [
	#path('data_fetching/', views.data_fetching, name='data_fetching'),
	#path('result/', views.result, name='result'),
    path('', views.index, name='index'),
]
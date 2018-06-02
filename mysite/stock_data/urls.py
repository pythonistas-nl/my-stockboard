from django.urls import path

from . import views

app_name = 'stock_data'
urlpatterns = [
	path('result/', views.result, name='result'),
    path('', views.index, name='index'),
]
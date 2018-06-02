from django.urls import path

from . import views

app_name = 'stock_data'
urlpatterns = [
    path('', views.index, name='index'),
]
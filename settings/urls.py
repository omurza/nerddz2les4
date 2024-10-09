from django.urls import path
from django.shortcuts import render
from settings.views import set_list

urlpatterns = [
    path('', set_list, name='set_list'),
	
]
from django.shortcuts import render
from django.urls import path
from .views import set_list

urlpatterns = [
    path('employ/', set_list, name='set_list'),
]
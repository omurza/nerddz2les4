from django.shortcuts import render
from .models import Setmodel,Galery

def set_list(request):
    setting= Setmodel.objects.latest("id")
    galary = Galery.objects.latest("id")
    return render(request, 'INDEX.HTML', locals())

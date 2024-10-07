from django.shortcuts import render

# Create your views here.
from .models import Setmodel

def set_list(request):
    employ = Setmodel.objects.all()
    return render(request, 'Setmodel/INDEX.HTML', {'Setmodel': Setmodel})

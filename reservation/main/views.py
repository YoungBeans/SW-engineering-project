from django.shortcuts import render , redirect, get_object_or_404
from login.models import *
from reserv.models import *


# Create your views here.
def home(request):
    Foods = Menu.objects.all()
    rest = get_object_or_404(Restaurant, name="갈풍집")
    food = get_object_or_404(Food, food='마늘갈비살')
    context = {"foods" : Foods, "Rest" : rest, 'site' : True}
    
    return render(request, "main/home.html", context)

from django.shortcuts import render
from .models import Bus
# Create your views here.



def home(request):
    return render(request,'home.html')


def bus_list(request):
    buses = Bus.objects.all()
    return render(request, 'bus_list.html', {'buses': buses})



from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Bus
# Create your views here.



def home(request):
    return render(request,'home.html')

@login_required
def bus_list(request):
    buses = Bus.objects.all()
    return render(request, 'bus_list.html', {'buses': buses})

@login_required()
def search_buses(request):
    if request.method == 'POST':
        source = request.POST.get('source', '')
        destination = request.POST.get('destination', '')
        travel_date = request.POST.get('travel_date', '')

        if travel_date:
            buses = Bus.objects.filter(
                route__origin__icontains=source,
                route__destination__icontains=destination,
                schedule__departure_time__date=travel_date
            )
        else:
            buses = Bus.objects.none()

        context = {
            'buses': buses,
            'source': source,
            'destination': destination,
            'travel_date': travel_date,
        }

        if not buses:
            context['no_buses_message'] = "No buses available for the given search criteria."

        return render(request, 'search.html', context)
    else:
        return render(request, 'search.html')

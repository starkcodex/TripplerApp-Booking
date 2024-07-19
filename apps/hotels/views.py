from django.shortcuts import render, redirect
from .models import Hotel
from .forms import HotelCreateForm

def hotelview(request):
    hotels = Hotel.objects.all()
    return render(request, 'hotel/hotel_list.html', {'hotels' : hotels})


def add_hotel(request):
    form = HotelCreateForm()
    
    if request.method == 'POST':
        form = HotelCreateForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('hotel')
        else:
            context = {'form': form}
    context = {'form': HotelCreateForm()}
    return render(request, 'hotel/add_hotel.html', context)
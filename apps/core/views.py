from django.shortcuts import render, redirect
from .models import Holiday
from bs4 import BeautifulSoup
import requests
from .forms import HolidayCreateForm


def homepage(request):
    holidays = Holiday.objects.all()
    return render(request, 'core/home_layout.html', {'holiday' : holidays})

def our_story(request):
    return render(request, 'includes/our_story.html')

def holiday_create(request):
    form = HolidayCreateForm()
    
    if request.method == 'POST':
        form = HolidayCreateForm(request.POST)
        if form.is_valid():
            holiday = form.save(commit=False)
            
            website = request.get(form.data['url'])
            sourcecode = BeautifulSoup(website.text, 'html.parser')
            
            find_image = sourcecode.select('meta[content="https://live.staticflicr.com/"]')
            image = find_image[0]['content']
            holiday.image = image
        
            find_title =  sourcecode.select('h1.photo-title')
            title = find_title[0].text.strip()
            holiday.title = title      
            
            find_artist =  sourcecode.select('a.owner-name')
            artist = find_artist[0].text.strip()
            holiday.artist = artist     
    
            holiday.save()
            return redirect('home')
        
    return render(request, 'holiday/holiday_create.html', {'form': form})



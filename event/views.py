from django.shortcuts import render
from show.models import Show

def event_page(request):
    shows = Show.objects.all()[0:8]
    return render(request, 'event/event_page.html', {'shows': shows})

def show(request):
    shows = Show.objects.all()
    return render(request, 'event/show.html', {'shows': shows})

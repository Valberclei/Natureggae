from django.shortcuts import render
from evento.models import Tourne

def tour_page(request):
    tournes = Tourne.objects.all()[0:8]
    return render(request, 'tour/tour_page.html', {'tournes': tournes})

def tour(request):
    tournes = Tourne.objects.all()

    return render(request, 'tour/tour.html', {'tournes': tournes})

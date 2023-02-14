from django.shortcuts import render, get_object_or_404

from .models import Evento

def evento(request, slug):
    evento = get_object_or_404(Evento, slug=slug)
    return render(request, 'evento/evento.html', {'evento': evento})
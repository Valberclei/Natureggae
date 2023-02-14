from django.db.models import Q
from django.shortcuts import render

from evento.models import Evento, Category

def tourpage(request):
    eventos = Evento.objects.all()[0:8]
    return render(request, 'tour/tourpage.html', {'eventos': eventos})

def tour(request):
    categories = Category.objects.all()
    eventos = Evento.objects.all()

    active_category = request.GET.get('category', '')

    if active_category:
        eventos = eventos.filter(category__slug=active_category)

    query = request.GET.get('query', '')

    if query:
        eventos = eventos.filter(Q(name__icontains=query) | Q(description__icontains=query))

    context = {
        'categories': categories,
        'eventos': eventos,
        'active_category': active_category
    }

    return render(request, 'tour/tourne.html', context)
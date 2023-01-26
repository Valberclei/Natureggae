from django.shortcuts import render

def show_evento(request):
    return render(request, 'shows/show_evento.html')
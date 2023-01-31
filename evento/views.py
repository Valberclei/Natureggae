from django.shortcuts import render

# Create your views here.
def evento(request):
    return render(request, 'evento/evento.html')
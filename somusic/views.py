from django.shortcuts import render

from django.core.paginator import Paginator
from .models import Song

def player(request):
    paginator = Paginator(Song.objects.all(), 1)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {"page_obj": page_obj}

    return render(request, "player.html", context)

def index(request):
    paginator = Paginator(Song.objects.all(), 1)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {"page_obj": page_obj}
    return render(request, "index.html", context)

def homepage(request):
    return render(request, "homepage.html")

def home_page(request):
    return render(request, "home_page.html")
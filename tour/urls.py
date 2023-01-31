from django.urls import path
from .views import tour_page, tour
from evento.views import evento

urlpatterns = [
    path('tour_page', tour_page, name='tour_page'),
    path('tour/', tour, name='tour'),
    path('evento/', evento, name='evento'),
]
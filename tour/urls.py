from django.urls import path
from .views import tour_page

urlpatterns = [
    path('tour_page', tour_page, name='tour_page'),
]
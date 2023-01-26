from django.urls import path

from event.views import event_page, show
from show.views import show_evento

urlpatterns = [
    path('event_page/', event_page, name='event_page'),
    path('show/', show, name='show'),
    path('show_evento/', show_evento, name='show_evento'),
]
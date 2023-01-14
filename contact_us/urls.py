from django.urls import path

from .views import *

urlpatterns = [
    path('enviar_contact/', enviar_contact, name='enviar_contact'),
    path('success_contact/', success_contact, name='success_contact'),
    path('listar_contacts/', listar_contacts, name='listar_contacts'),
    path('remover_contact/<int:id>', remover_contact, name='remover_contact'),
]
from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('listar_workers/', listar_workers, name='listar_workers'),
    path('cadastrar_worker/', cadastrar_worker, name='cadastrar_worker'),
    path('success/', success, name='success'),
    path('atualizar_worker/<int:id>', atualizar_worker, name='atualizar_worker'),

]
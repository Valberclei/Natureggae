from django.urls import path, include
from .views import *

urlpatterns = [
    path('listar_candidatos/', listar_candidatos, name='listar_candidatos'),
    path('cadastrar_candidato/', cadastrar_candidato, name='cadastrar_candidato'),
    path('editar_candidato/<int:id>', editar_candidato, name='editar_candidato'),
    path('remover_candidato/<int:id>', remover_candidato, name='remover_candidato'),

]
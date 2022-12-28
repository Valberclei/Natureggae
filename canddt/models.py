from django.db import models

class Candidato(models.Model):
    SEXO_CHOICES = [
        ("M", "Masculino"),
        ("F", "Feminino"),
    ]

    NIVEL_CHOICES = [
        ("S", "SENIOR"),
        ("P", "PLENO"),
        ("J", "JUNIOR"),
    ]
    nome = models.CharField(max_length=50, null=False, blank=False)
    sexo = models.CharField(max_length=1, choices=SEXO_CHOICES, null=False, blank=False)
    idade = models.CharField(max_length=2, null=False, blank=False)
    nivel = models.CharField(max_length=1, choices=NIVEL_CHOICES, null=False, blank=False)
    formacao = models.CharField(max_length=50, null=False, blank=False)
    pix = models.CharField(max_length=50, null=True, blank=True)
    celular = models.CharField(max_length=14, null=False, blank=False)
    # aula 2 min 1:14:00

from django.db import models

# Create your models here.

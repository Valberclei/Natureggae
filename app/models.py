from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Musica(models.Model):
    titulo = models.CharField(max_length=30, null=False, blank=False)
    usuario = models.ForeignKey(User, null=True, on_delete=models.CASCADE)

class PostImage(models.Model):
    title = models.TextField(max_length=200, null=True, blank=True)
    cover = models.ImageField(upload_to='images/')
    def __str__(self):
      return self.title

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
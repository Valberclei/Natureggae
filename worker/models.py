from django.db import models

class Worker(models.Model):
    SEX_CHOICES = [
        ("F", "Feminino"),
        ("M", "Masculino"),
    ]

    AREA_CHOICES = [
        ("T", "Tecnologia"),
        ("S", "Segurança"),
        ("M", "Musico"),
    ]

    LEVEL_CHOICES = [
        ("P", "Profissional"),
        ("I", "iniciante"),
        ("J", "Junior"),
        ("P", "Pleno"),
        ("S", "Senior"),
    ]
    nome = models.CharField(max_length=40, null=False, blank=False)
    email = models.EmailField(max_length=40, null=False, blank=False)
    address = models.CharField(max_length=55, null=False, blank=False)
    data_nas = models.DateField(null=False, blank=False)
    sex = models.CharField(max_length=1, choices=SEX_CHOICES, null=False, blank=False)
    area = models.CharField(max_length=1, choices=AREA_CHOICES, null=False, blank=False)
    level = models.CharField(max_length=1, choices=LEVEL_CHOICES, null=False, blank=False)
    phone = models.CharField(max_length=13, null=False, blank=False)
    link_social = models.CharField(max_length=155, null=True, blank=False)


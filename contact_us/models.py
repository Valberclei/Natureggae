from django.db import models

class Contact(models.Model):
    nome = models.CharField(max_length=40, null=False, blank=False)
    email = models.EmailField(max_length=40, null=False, blank=False)
    message = models.TextField(max_length=255, null=False, blank=False)
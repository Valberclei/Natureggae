from django.db import models

class Show_tipo(models.Model):
    name = models.CharField(max_length=30)
    slug = models.SlugField()
    local = models.CharField(max_length=100)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name

class Tourne(models.Model):

    show_tipo = models.ForeignKey(Show_tipo, related_name='tourne', on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    slug = models.SlugField()
    local = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-created_at',)

    def __str__(self):
        return self.local

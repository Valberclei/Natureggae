from django.db import models

class Tipo(models.Model):
    name = models.CharField(max_length=25)
    slug = models.SlugField()

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name

class Show(models.Model):
    tipo = models.ForeignKey(Tipo, related_name='shows', on_delete=models.CASCADE)
    name = models.CharField(max_length=25)
    slug = models.SlugField()
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-created_at',)

        def __str__(self):
            return self.name
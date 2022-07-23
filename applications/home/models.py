from django.db import models


# Create your models here.
class HomeModel(models.Model):
    """class model that represent a table in database"""

    """define the attrs"""
    titulo = models.CharField(max_length=100)
    subtitulo = models.CharField(max_length=50)
    cantidad = models.IntegerField()

    def __str__(self):
        return (
            f"title: {self.titulo} - subtitle: {self.subtitulo} - cant {self.cantidad}"
        )

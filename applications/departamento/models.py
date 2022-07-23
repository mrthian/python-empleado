from django.db import models


# Create your models here.
class DepartamentoModel(models.Model):
    """class model of Departamento"""
    class Meta:
        verbose_name = 'deparment'
        verbose_name_plural = 'deparments'
        ordering = ['name']  # allow ordering
        # unique_together = ('name', 'short_name')  # Crear una unique index.

    name = models.CharField('Nombre', max_length=50, blank=False)
    short_name = models.CharField('Nombre Corto', max_length=20, blank=False, unique=True)
    state = models.BooleanField('Anulado', default=False)
    create_at = models.DateTimeField('Create At', auto_created=True, auto_now_add=True)

    def __str__(self):
        return f"{self.id} | {self.name} | {self.short_name} | {self.state}"
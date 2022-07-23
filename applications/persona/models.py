from django.db import models
from applications.departamento.models import DepartamentoModel

from ckeditor.fields import RichTextField


# Create your models here.
class HabilidadModel(models.Model):

    class Meta:
        verbose_name = 'Habilidad'
        verbose_name_plural = 'Habilidades'

    habilidad = models.CharField('Habilidad', max_length=50)

    def __str__(self):
        return f"{self.id} - {self.habilidad}"


class PersonaModel(models.Model):
    """Model of empleado"""

    class Meta:
        verbose_name = 'Empleado'
        verbose_name_plural = 'Empleados'

    JOB_CHOICES = (
        ('-1', 'Seleccionar'),
        ('0', 'Contador'),
        ('1', 'Administrador'),
        ('2', 'Sistemas'),
        ('3', 'Economista'),
        ('4', 'Otro'),
    )

    first_name = models.CharField('Nombres', max_length=150, blank=False)
    last_name = models.CharField('Apellidos', max_length=150, blank=False)
    full_name = models.CharField('Nombre Completo', max_length=300, blank=True)
    job = models.CharField('Cargo', max_length=5, choices=JOB_CHOICES, default='-1')
    departamento = models.ForeignKey(DepartamentoModel, on_delete=models.RESTRICT)
    avatar = models.ImageField(upload_to='media/persona', blank=True, null=True)
    habilidad = models.ManyToManyField(HabilidadModel)
    cv = RichTextField()

    def __str__(self):
        return f"{self.first_name} - {self.last_name} - {self.job} - {self.departamento.name}"


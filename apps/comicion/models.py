from django.db import models
from apps.usuario.models import Docente


# Create your models here.
class ComicionDeSeguimiento(models.Model):

    nroResolucion = models.CharField(max_length=15, unique=True)
    docentes = models.ManyToManyField(Docente)
    fechaDeComicion = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ['fechaDeComicion']

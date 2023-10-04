from django.db import models
from apps.usuario.models import Docente


# Create your models here.

class TribunalEvaluador(models.Model):
    ROLES_OPCIONES = (
        ('PRESIDENTE', 'Presidente'),
        ('VOCAL_TITULAR', 'Vocal Titular'),
        ('VOCAL_SUPLENTE', 'Vocal Suplente')
    )

    nroResolucion = models.CharField(max_length=15, unique=True)
    fechaTribunal = models.DateField(auto_now_add=True)
    docentes = models.ManyToManyField(Docente)
    NRO_DOCENTES = 5
    rol = models.CharField(max_length=15, choices=ROLES_OPCIONES)

    class Meta:
        ordering = ['fechaTribunal']

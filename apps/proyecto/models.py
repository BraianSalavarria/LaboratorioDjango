from django.db import models
from apps.usuario.models import Docente
from apps.usuario.models import Alumno


# Create your models here.

class ProyectoTrabajoFinal(models.Model):
    ROL_OPCIONES = (
        ('DIRECTOR', 'Director'),
        ('CO-DIRECTOR', 'Co-Director'),
        ('ASCESOR', 'Ascesor')
    )

    titulo = models.CharField(max_length=40, unique=True)
    fechaPresentacion = models.DateField()
    descripcion = models.TextField(max_length=500)
    NroResolucionTribunal = models.CharField(max_length=15)
    rolDocente = models.CharField(max_length=12, choices=ROL_OPCIONES)
    docentes = models.ManyToManyField(Docente)
    alumno = models.ForeignKey(Alumno, on_delete=models.CASCADE)
    archivosAdjuntos = models.FileField(upload_to='Files/ArchivosDePTF/', blank=False, null=False, default=None)

    class Meta:
        ordering = ['fechaPresentacion']

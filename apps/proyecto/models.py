from django.db import models
from apps.persona.models import Docente
from apps.persona.models import Alumno
from apps.persona.models import Ascesor

# Create your models here.


class ProyectoTrabajoFinal(models.Model):
    ROL_OPCIONES = (
        ('DIRECTOR', 'Director'),
        ('CO-DIRECTOR', 'Co-Director'),
    )

    titulo = models.CharField(max_length=40, unique=True)
    fechaPresentacion = models.DateField()
    descripcion = models.TextField(max_length=500)
    NroResolucionTribunal = models.CharField(max_length=15)
    rolDocente = models.CharField(max_length=12, choices=ROL_OPCIONES)
    archivosAdjuntos = models.FileField(upload_to='Files/ArchivosDePTF/', blank=False, null=False, default=None)
    docentes = models.ManyToManyField(Docente)
    alumno = models.ForeignKey(Alumno, on_delete=models.CASCADE)
    ascesor = models.ForeignKey(Ascesor, on_delete=models.CASCADE, null=True)

    class Meta:
        ordering = ['fechaPresentacion']


class MovimientosPTF(models.Model):
    MOVIMIENTOS_OPCIONES = (
        ('PROYECTO_PRESENTADO', 'Proyecto Presentado - Esperando Evaluacion por CSTF'),
        ('PROYECTO_EVALUADO_POR_CSTF', 'Proyectado Evaluado por la CSTF'),
        ('PROYECTO_EN_EVALUACION_POR_EL_TRIBUNAL', 'Proyecto en Evaluacion por el Tribunal'),
        ('PROYECTO_EVALUADO_POR_EL_TRIBUNAL', 'Proyecto Evaluado por el Tribunal'),
        ('PROYECTO_APROBADO', 'Proyecto Aprobado')
    )

    fechaDeMovimiento = models.DateTimeField()
    proyectoTrabajoFinal = models.ForeignKey(ProyectoTrabajoFinal, on_delete=models.CASCADE)

    class Meta:
        ordering = ['fechaDeMovimiento']

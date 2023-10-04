from django.db import models
from apps.tribunal.models import TribunalEvaluador
from apps.comicion.models import ComicionDeSeguimiento
from apps.proyecto.models import ProyectoTrabajoFinal


class AbstractInforme(models.Model):

    ESTADO_OPCIONES = (
        ('ACEPTADO', 'Aceptado'),
        ('RECHAZADO', 'Rechazado'),
        ('OBSERVADO', 'Observado')
    )
    fechaInforme = models.DateField(auto_now_add=True)
    estado = models.CharField(max_length=10, choices=ESTADO_OPCIONES)

    class Meta:
        abstract = True
        ordering = ['fechaInforme']


class InformeEvaluacionPTF(AbstractInforme):

    tribunalElavaluador = models.ForeignKey(TribunalEvaluador, on_delete=models.CASCADE)
    proyectoTrabajoFinal = models.ForeignKey(ProyectoTrabajoFinal, on_delete=models.CASCADE)
    archivosAdjuntos = models.FileField(upload_to='Files/ArchivosDeInformes/', blank=False, null=False, default=None)


class InformeEvaluacionFormalPTF(AbstractInforme):

    descripcion = models.TextField(max_length=500)
    plazoObservacion = models.DateField()
    comicionSeguimiento = models.ForeignKey(ComicionDeSeguimiento, on_delete=models.CASCADE)
    proyectoTrabajoFinal = models.ForeignKey(ProyectoTrabajoFinal, on_delete=models.CASCADE)

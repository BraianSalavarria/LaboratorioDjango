from django.db import models
from apps.proyecto.models import ProyectoTrabajoFinal
from apps.persona.models import Docente


class ComicionDeSeguimiento(models.Model):
    nroResolucion = models.CharField(max_length=15, unique=True)
    fechaDeComicion = models.DateField()

    class Meta:
        ordering = ['fechaDeComicion']

    def __str__(self):
        return f'{self.nroResolucion}'


class TribunalEvaluador(models.Model):
    nroResolucion = models.CharField(max_length=15, unique=True)
    fechaTribunal = models.DateField()

    class Meta:
        ordering = ['fechaTribunal']
        
    def __str__(self) -> str:
        return f'{self.nroResolucion}'


class IntegrantesTribunal(models.Model):
    nroResolucionTribunal = models.ForeignKey(TribunalEvaluador,on_delete=models.CASCADE)
    TIPO_OPCIONES = (
        ('PRESIDENTE', 'Presidente'),
        ('VOCAL_TITULAR', 'Vocal Titular'),
        ('VOCAL_SUPLENTE', 'Vocal Suplente')
    )
    integrante = models.ForeignKey(Docente, on_delete=models.CASCADE)
    tipo = models.CharField(max_length=15, choices=TIPO_OPCIONES)


class IntegrantesComicion(models.Model):
    nroResolucionComicion = models.ForeignKey(ComicionDeSeguimiento, on_delete=models.CASCADE)
    integrante = models.ForeignKey(Docente, on_delete=models.CASCADE)


class AbstractInforme(models.Model):
    ESTADO_OPCIONES = (
        ('ACEPTADO', 'Aceptado'),
        ('RECHAZADO', 'Rechazado'),
        ('OBSERVADO', 'Observado')
    )
    observacion = models.TextField(max_length=500)
    fechaInforme = models.DateField()
    estado = models.CharField(max_length=10, choices=ESTADO_OPCIONES)

    class Meta:
        abstract = True
        ordering = ['fechaInforme']


class InformeEvaluacionPTF(AbstractInforme):
    tribunalElavaluador = models.ForeignKey(TribunalEvaluador, on_delete=models.CASCADE)
    proyectoTrabajoFinal = models.ForeignKey(ProyectoTrabajoFinal, on_delete=models.CASCADE)
    archivosAdjuntos = models.FileField(upload_to='Files/ArchivosDeInformes/', blank=False, null=False, default=None)


class InformeEvaluacionFormalPTF(AbstractInforme):
    plazoObservacion = models.DateField(blank=True, null=True)
    comicionSeguimiento = models.ForeignKey(ComicionDeSeguimiento, on_delete=models.CASCADE)
    proyectoTrabajoFinal = models.ForeignKey(ProyectoTrabajoFinal, on_delete=models.CASCADE)

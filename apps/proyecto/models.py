from django.db import models
from apps.persona.models import Alumno#,Docente,Ascesor,
from apps.evaluacion.models import ComicionDeSeguimiento,ProyectoTrabajoFinal #,TribunalEvaluador
from datetime import date

# Create your models here.

"""
class ProyectoTrabajoFinal(models.Model):

    titulo = models.CharField(max_length=40, unique=True)
    fechaPresentacion = models.DateField(default=date.today)
    descripcion = models.TextField(max_length=500)
    #NroResolucionTribunal = models.ForeignKey(TribunalEvaluador,on_delete=models.CASCADE)
    archivosAdjuntos = models.FileField(upload_to='Files/ArchivosDePTF/', blank=False, null=False, default=None)
    director = models.ForeignKey(Docente, on_delete=models.CASCADE, related_name='director')
    coDirector = models.ForeignKey(Docente, on_delete=models.CASCADE, related_name='codirector')
    ascesor = models.ForeignKey(Ascesor, on_delete=models.CASCADE,null=True,blank=True)

    class Meta:
        ordering = ['fechaPresentacion']

    def __str__(self) -> str:
        return f'{self.titulo}'
"""
class IntegrantesPTF(models.Model):
    proyectoTrabajoFinal = models.ForeignKey(ProyectoTrabajoFinal, on_delete=models.CASCADE)
    integrante = models.ForeignKey(Alumno, on_delete=models.CASCADE)
    fechaAlta = models.DateField(default=date.today)
    fechaBaja = models.DateField(null=True,blank=True)

    def __str__(self) -> str:
        if self.fechaBaja == None:
            return f'El alumno {self.integrante} se encuentra dado de ALTA en el proyecto {self.proyectoTrabajoFinal}'
        else:
            return f'El alumno {self.integrante} se encuentra dado de BAJA en el proyecto {self.proyectoTrabajoFinal}'
class MovimientosPTF(models.Model):
    MOVIMIENTOS_OPCIONES = (
        ('PROYECTO_PRESENTADO', 'Proyecto Presentado - Esperando Evaluacion por CSTF'),
        ('PROYECTO_EVALUADO_POR_CSTF', 'Proyectado Evaluado por la CSTF'),
        ('PROYECTO_EN_EVALUACION_POR_EL_TRIBUNAL', 'Proyecto en Evaluacion por el Tribunal'),
        ('PROYECTO_EVALUADO_POR_EL_TRIBUNAL', 'Proyecto Evaluado por el Tribunal'),
        ('PROYECTO_APROBADO', 'Proyecto Aprobado')
    )
    movimiento = models.CharField(max_length=51, choices=MOVIMIENTOS_OPCIONES)
    proyectoTrabajoFinal = models.ForeignKey(ProyectoTrabajoFinal, on_delete=models.CASCADE)
    fechaDeMovimiento = models.DateField(default=date.today)
    fechaVencimientoMovimiento = models.DateField(blank=True,null=True)
    archivosAdjuntoOpcional = models.FileField(upload_to='Files/ArchivosDeMovimientos/', blank=True,null=True)

    class Meta:
        ordering = ['fechaDeMovimiento']

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
    proyectoTrabajoFinal = models.ForeignKey(ProyectoTrabajoFinal, on_delete=models.CASCADE)
    archivosAdjuntos = models.FileField(upload_to='Files/ArchivosDeInformes/', blank=False, null=False, default=None)


class InformeEvaluacionFormalPTF(AbstractInforme):
    plazoObservacion = models.DateField(blank=True, null=True)
    comicionSeguimiento = models.ForeignKey(ComicionDeSeguimiento, on_delete=models.CASCADE)
    proyectoTrabajoFinal = models.ForeignKey(ProyectoTrabajoFinal, on_delete=models.CASCADE)
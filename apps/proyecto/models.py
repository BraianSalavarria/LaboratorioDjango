from django.db import models
from apps.persona.models import Docente,Ascesor,Alumno
from datetime import date

# Create your models here.


class ProyectoTrabajoFinal(models.Model):

    titulo = models.CharField(max_length=40, unique=True)
    fechaPresentacion = models.DateField(default=date.today)
    descripcion = models.TextField(max_length=500)
    NroResolucionTribunal = models.CharField(max_length=15)
    archivosAdjuntos = models.FileField(upload_to='Files/ArchivosDePTF/', blank=False, null=False, default=None)
    director = models.ForeignKey(Docente, on_delete=models.CASCADE, related_name='director')
    coDirector = models.ForeignKey(Docente, on_delete=models.CASCADE, related_name='codirector')
    ascesor = models.ForeignKey(Ascesor, on_delete=models.CASCADE,null=True,blank=True)

    class Meta:
        ordering = ['fechaPresentacion']

    def __str__(self) -> str:
        return f'{self.titulo}'

class IntegrantesPTF(models.Model):
    proyectoTrabajoFinal = models.ForeignKey(ProyectoTrabajoFinal, on_delete=models.CASCADE)
    integrante = models.ForeignKey(Alumno, on_delete=models.CASCADE)
    fechaAlta = models.DateField(default=date.today)
    fechaBaja = models.DateField(null=True,blank=True)


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
    fechaDeMovimiento = models.DateField()
    fechaVencimientoMovimiento = models.DateField(blank=True,default=date.today)
    archivosAdjuntoOpcional = models.FileField(upload_to='Files/ArchivosDeMovimientos/', blank=True)

    class Meta:
        ordering = ['fechaDeMovimiento']

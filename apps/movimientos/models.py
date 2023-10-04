from django.db import models
from apps.proyecto.models import ProyectoTrabajoFinal


class MovimientosPTF(models.Model):
    MOVIMIENTOS_OPCIONES = (
        ('PROYECTO_PRESENTADO', 'Proyecto Presentado - Esperando Evaluacion por CSTF'),
        ('PROYECTO_EVALUADO_POR_CSTF', 'Proyectado Evaluado por la CSTF'),
        ('PROYECTO_EN_EVALUACION_POR_EL_TRIBUNAL', 'Proyecto en Evaluacion por el Tribunal'),
        ('PROYECTO_EVALUADO_POR_EL_TRIBUNAL', 'Proyecto Evaluado por el Tribunal'),
        ('PROYECTO_APROBADO', 'Proyecto Aprobado')
    )

    fechaDeMovimiento = models.DateTimeField(auto_now_add=True)
    proyectoTrabajoFinal = models.ForeignKey(ProyectoTrabajoFinal, on_delete=models.CASCADE)

    class Meta:
        ordering = ['fechaDeMovimiento']

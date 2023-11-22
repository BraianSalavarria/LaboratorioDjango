from django.db import models
from apps.persona.models import Docente,Ascesor
#from apps.proyecto.models import ProyectoTrabajoFinal
from datetime import date



class ComicionDeSeguimiento(models.Model):
    nroResolucion = models.CharField(max_length=15, unique=True)
    fechaDeComicion = models.DateField()

    class Meta:
        ordering = ['fechaDeComicion']

    def __str__(self):
        return f'{self.nroResolucion}'

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
class TribunalEvaluador(models.Model):
    nroResolucion = models.CharField(max_length=15, unique=True)
    fechaTribunal = models.DateField()
    trabajo_final = models.ForeignKey(ProyectoTrabajoFinal,on_delete=models.SET_NULL,null=True)

    class Meta:
        ordering = ['fechaTribunal']

    def __str__(self) -> str:
        return self.nroResolucion
class IntegrantesTribunal(models.Model):
    nroResolucionTribunal = models.ForeignKey(TribunalEvaluador, on_delete=models.CASCADE)
    TIPO_OPCIONES = (
        ('PRESIDENTE', 'Presidente'),
        ('VOCAL_TITULAR', 'Vocal Titular'),
        ('VOCAL_SUPLENTE', 'Vocal Suplente')
    )
    integrante = models.ForeignKey(Docente, on_delete=models.CASCADE)
    tipo = models.CharField(max_length=15, choices=TIPO_OPCIONES)


class IntegrantesComicion(models.Model):
    nroResolucioncomicion = models.ForeignKey(ComicionDeSeguimiento, on_delete=models.CASCADE)
    integrante = models.ForeignKey(Docente, on_delete=models.CASCADE)




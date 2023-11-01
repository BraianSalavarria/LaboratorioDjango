from django.db import models
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




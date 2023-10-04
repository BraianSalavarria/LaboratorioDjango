from django.db import models


class AbstractPersona(models.Model):
    nombre = models.CharField(max_length=80)
    apellido = models.CharField(max_length=90)

    class Meta:
        abstract = True
        ordering = ['nombre', 'apellido']

    def __str__(self):
        return f'{self.nombre} {self.apellido}'


class Alumno(AbstractPersona):
    dni = models.CharField(max_length=8, unique=True)
    correoElectronico = models.EmailField(max_length=256, blank=False, null=False)


class Docente(AbstractPersona):
    cuil = models.CharField(max_length=11, unique=True)

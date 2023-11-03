from django.db import models
from django.contrib.auth.models import User


class AbstractPersona(models.Model):
    nombre = models.CharField(max_length=80)
    apellido = models.CharField(max_length=90)
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)

    class Meta:
        abstract = True
        ordering = ['nombre', 'apellido']

    def add_user(self,user):
        self.user = user

class Alumno(AbstractPersona):
    dni = models.CharField(max_length=8, unique=True)
    matricula = models.CharField(unique=True)
    correoElectronico = models.EmailField(max_length=256, blank=False, null=False)
    
    def __str__(self) -> str:
        return f'{self.nombre} {self.apellido} - {self.matricula}'


class Docente(AbstractPersona):
    cuil = models.CharField(max_length=11, unique=True)

    def __str__(self):
        return f'{self.nombre} {self.apellido} - {self.cuil}'


class Ascesor(AbstractPersona):
    cuil = models.CharField(max_length=11, unique=True)
    curriculum = models.FileField(upload_to='Files/CurriculumAscesor/')
    
    def __str__(self) -> str:
        return f'{self.nombre} {self.apellido} - {self.cuil}'

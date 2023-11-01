from django.db import models



# Create your models here.

class Usuario(models.Model):
    USUARIOS_OPCIONES = (
        ('USUARIO_ADMIN', 'Usuario Administrador'),
        ('USUARIO_CSTF', 'Usuario CSTF'),
        ('USUARIO_TE', 'Usuario TE'),
        ('USUARIO_ALUMNO', 'Usuario Alumno'),
    )
    tipo = models.CharField(max_length=30, choices=USUARIOS_OPCIONES)
    username = models.CharField()
    password = models.CharField()
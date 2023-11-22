from django.contrib.auth.models import User, Group, Permission
from django.db.models.signals import post_migrate
from django.dispatch import receiver
import logging
logger = logging.getLogger(__name__)

@receiver(post_migrate)
def crear_superusuario(sender, **kwargs):
    if sender.name == 'apps.usuarios' and User.objects.filter(username='admin').count() == 0:
        User.objects.create_superuser('admin', 'admin@example.com', '1234')
        logger.debug("Super usuario generado")

@receiver(post_migrate)
def crear_grupos_y_permisos(sender, **kwargs):
    if sender.name == 'apps.usuarios':
        # Crea el grupo si no existe
        nuevo_grupo_comision, creado_comision = Group.objects.get_or_create(name='comision')
        nuevo_grupo_tribunal, creado_tribunal = Group.objects.get_or_create(name='tribunal')
        nuevo_grupo_alumno, creado_alumno = Group.objects.get_or_create(name='alumno')

        # Asigno permisos al grupo comision
        permisos_comision = Permission.objects.filter(content_type__app_label='persona', codename__in=['add_docente', 'add_alumno'])
        permisos_comision2 = Permission.objects.filter(content_type__app_label='evaluacion', codename__in=['add_proyectotrabajofinal','add_integrantestribunal','view_tribunalevaluador'])
        permisos_comision3 = Permission.objects.filter(content_type__app_label='proyecto', codename__in=['add_informeevaluacionformalptf'])
        permisos_combinados = list(permisos_comision) + list(permisos_comision2) + list(permisos_comision3)
        nuevo_grupo_comision.permissions.set(permisos_combinados)
        nuevo_grupo_comision.save()
        logger.debug(f'{nuevo_grupo_comision} -> grupo creado con los siguientes permisos: {permisos_combinados}')
        
        # Permisos de alumno
        permisos_alumno = Permission.objects.filter(content_type__app_label='evaluacion', codename__in=['view_proyectotrabajofinal'])
        nuevo_grupo_alumno.permissions.set(permisos_alumno)
        nuevo_grupo_alumno.save()
        logger.debug(f'{nuevo_grupo_alumno} -> grupo creado con los siguientes permisos: {permisos_alumno}')
        
        #Permisos de tribunal
        permisos_tribunal = Permission.objects.filter(content_type__app_label='proyecto', codename__in=['add_informeevaluacionptf'])
        permisos_tribunal2 = Permission.objects.filter(content_type__app_label='evaluacion', codename__in=['view_proyectotrabajofinal','view_tribunalevaluador'])
        permisos_combinados_tribunal = list(permisos_tribunal) + list(permisos_tribunal2)
        nuevo_grupo_tribunal.permissions.set(permisos_combinados_tribunal)
        nuevo_grupo_tribunal.save()
        logger.debug(f'{nuevo_grupo_tribunal} -> grupo creado con los siguientes permisos: {permisos_tribunal}')
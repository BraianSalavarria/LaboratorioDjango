from apps.persona.models import Alumno,Docente
from django.contrib.auth.models import User
import logging
logger = logging.getLogger(__name__)
def usuario(request):
    url_completa = request.get_full_path()
    
    if '/login' not in url_completa:
        username = request.user
        user = User.objects.get(username=username)
        logger.debug(f'Usuer: {user}')
        objetos = list(Alumno.objects.filter(user=user)) + list(Docente.objects.filter(user=user))
        logger.debug(f'Objetos: {objetos}')
        persona = None
        try:
            persona = objetos[0]
        except Exception as e:
            logger.debug(f'Excepcion: {e}')
        logger.debug(f'User: {user.username}')
        if persona is not None:
            logger.debug(f'Persona: {persona.nombre}')
            return {'username':username,'nombre':persona.nombre,'apellido':persona.apellido}
        return {'username':user.username,'nombre':'Nombre','apellido':'Apellido'}
    else:
        return {}
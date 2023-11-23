from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,logout as logoutApp, login as loginApp
from apps.persona.models import Alumno, Docente
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from apps.proyecto.models import IntegrantesPTF,MovimientosPTF
from apps.evaluacion.models import ProyectoTrabajoFinal, IntegrantesTribunal,TribunalEvaluador
import logging
logger = logging.getLogger(__name__)

@login_required(login_url="/login")
def home(request): 
    persona = None
    if not request.user.is_authenticated:
        return redirect('/login')
    username = request.user
    user = User.objects.get(username=username)
    logger.debug(f'Usuer: {user}')
    objetos = list(Alumno.objects.filter(user=user)) + list(Docente.objects.filter(user=user))
    try:
        persona = objetos[0]
    except Exception as e:
        logger.debug(f'Excepcion: {e}')
    #if isinstance(persona, Docente):
    #   if user.has_perm('')
    if persona is not None:
        if isinstance(persona,Alumno):
            if user.has_perm('evaluacion.view_proyectotrabajofinal'):
                context = obtener_info_alumno(persona.id)
                return render(request, 'base/base.html',context)
        elif isinstance(persona,Docente):
            context = obtener_info_docente(persona.id)
            return render(request, 'base/base.html',context)
    return render(request, 'base/base.html')

def login(request):
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]
        logger.debug(f'Credenciales[ username: {username}, password:{password}]')
        user = authenticate(username = username,password = password)
        if user is not None:
            logger.debug(user)
            loginApp(request,user)
            return redirect('/')    
    return render(request, 'login/login.html')

def logout(request):
    if request.method == 'POST':
        persona = request.user
        logger.debug(f'{persona.username} esta cerrando sesion')
        logger.debug('Redirigiendo a login...')
        logoutApp(request)
        return redirect('/login')
    
def pagina_no_encontrada(request, exception):
    return render(request, 'base/404.html', status=404)

def obtener_info_alumno(id):
    proyecto_integrantes = IntegrantesPTF.objects.filter(integrante_id=id).first()
    proyecto = ProyectoTrabajoFinal.objects.get(pk=proyecto_integrantes.proyectoTrabajoFinal.id)
    movimientos_list = MovimientosPTF.objects.filter(proyectoTrabajoFinal=proyecto)
    
    return {'proyecto':proyecto,'movimientos':movimientos_list}
    
def obtener_info_docente(id):
    listado_proyectos_a_evaluar = []
    docente = Docente.objects.get(pk=id)
    user = docente.user
    if user.has_perm('proyecto.add_informeevaluacionptf'): #El docente forma parte de un tribunal evaluador
        tribunales = IntegrantesTribunal.objects.filter(integrante=docente) #Tribunales en los cuales el docente es parte
        
        for tribunal in tribunales:
            tribunal_evaluador = TribunalEvaluador.objects.get(pk=tribunal.id)
            proyecto = tribunal_evaluador.trabajo_final
            logger.debug(f'Se ha encontrado el proyecto: {proyecto}')
            movimiento = MovimientosPTF.objects.filter(proyectoTrabajoFinal=proyecto,movimiento='PROYECTO_EN_EVALUACION_POR_EL_TRIBUNAL') #el proyecto tiene que estar aprobado por la comision
            if len(movimiento) > 0:
                listado_proyectos_a_evaluar.append(proyecto)
                logger.debug(f'Se ha añadido el proyecto: {proyecto} al contexto')
            else:
                logger.debug(f'El proyecto: {proyecto} no esta aprobado por la comision')
    context = {'proyectos':listado_proyectos_a_evaluar}
    return context
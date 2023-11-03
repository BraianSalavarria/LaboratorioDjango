from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,logout as logoutApp, login as loginApp
from apps.persona.models import Alumno, Docente
from django.contrib.auth.models import User
import logging
logger = logging.getLogger(__name__)

def home(request):
    if not request.user.is_authenticated:
        return redirect('/login')
    user = request.user
    objetos = list(Alumno.objects.filter(user=user)) + list(Docente.objects.filter(user=user))
    persona = None
    try:
        persona = objetos[0]
    except Exception as e:
        logger.debug(e)
    logger.debug(f'User: {user.username}')
    if persona is not None:
        logger.debug(f'Persona: {persona.nombre}')
    return render(request, 'base/base.html',{'username':user.username})

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
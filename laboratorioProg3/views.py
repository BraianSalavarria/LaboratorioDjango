from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,logout as logoutApp, login as loginApp
from apps.persona.models import Alumno, Docente
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
import logging
logger = logging.getLogger(__name__)

@login_required(login_url="/login")
def home(request):
    if not request.user.is_authenticated:
        return redirect('/login')
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
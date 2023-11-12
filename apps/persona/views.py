import random
import string
from django.core.mail import send_mail
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from .forms import AlumnoForm, DocenteForm, AsesorForm
from .models import Alumno, Docente, Ascesor
from django.contrib.auth.decorators import login_required,permission_required
import logging
logger = logging.getLogger(__name__)

def generar_username(nombre, apellido):
    primera_letra = nombre[0].lower()
    username = primera_letra + apellido
    return username

def generar_password(longitud):
    caracteres_validos = string.ascii_letters + string.digits
    password = ''.join(random.choice(caracteres_validos) for _ in range(longitud))
    return password

def enviar_email(destinatario,usuario,password):
    subject = 'Nuevo usuario'
    message = f'Bienvenido/a al sistema Gestion TF, tus credenciales de acceso son: Usuario: {usuario} , Contraseña: {password}'
    from_email = 'comision.unca@hotmail.com'
    recipient_list = [destinatario]
    send_mail(subject, message, from_email, recipient_list)

@login_required(login_url="/login")
@permission_required("persona.view_alumno")
def registrar_alumno(request):
    nuevo_alumno = None
    if request.method == 'POST':
        nombre = request.POST['nombre']
        apellido = request.POST['apellido']
        username = generar_username(nombre, apellido)
        logger.debug(f'Username generado: {username}')
        password = generar_password(10)
        logger.debug(f'Password generada: {password}')
        registrar_alumno_form = AlumnoForm(request.POST)
        if registrar_alumno_form.is_valid():
            user = User.objects.create_user(username,password= password)
            logger.debug(f'User: {user}')
            nuevo_alumno = registrar_alumno_form.save(commit=True)
            logger.debug(nuevo_alumno)
            nuevo_alumno.user = user
            nuevo_alumno.save()
            enviar_email(nuevo_alumno.correoElectronico,username, password)
            messages.success(request, f'se ha registrado el alumno {nuevo_alumno} correctamente')
    else:
        registrar_alumno_form = AlumnoForm()
    return render(request, 'persona/registroAlumnos.html', {'form': registrar_alumno_form})


def registrar_docente(request):
    nuevo_docente = None
    if request.method == 'POST':
        nombre = request.POST['nombre']
        apellido = request.POST['apellido']
        username = generar_username(nombre, apellido)
        password = generar_password(10)
        registrar_docente_form = DocenteForm(request.POST)
        if registrar_docente_form.is_valid():
            user = User.objects.create_user(username,password= password)
            nuevo_docente = registrar_docente_form.save(commit=True)
            nuevo_docente.user = user
            nuevo_docente.save()
            enviar_email(nuevo_docente.correoElectronico,username, password)
            messages.success(request, f'se ha registrado el docente {nuevo_docente} correctamente')
    else:
        registrar_docente_form = DocenteForm()     
    return render(request, 'persona/registroDocente.html', {'form': registrar_docente_form})


def registrar_ascesor(request):
    nuevo_asesor = None
    if request.method == 'POST':
        registrar_asesor_form = AsesorForm(request.POST, request.FILES)
        if registrar_asesor_form.is_valid():
            nuevo_asesor = registrar_asesor_form.save(commit=True)
            messages.success(request, f'se ha registrado el asesor {nuevo_asesor} correctamente')
    else:
        registrar_asesor_form = AsesorForm()
    return render(request, 'persona/registroAscesor.html', {'form': registrar_asesor_form})


def dar_baja_alumno(request):
    mensaje = ''
    if request.method == 'POST':
        if 'dni' in request.POST:
            alumno = get_object_or_404(Alumno, dni=request.POST['dni'])
            alumno.delete()
            mensaje = 'Operación exitosa'
    return render(request, 'persona/darBajaAlumno.html', {'mensaje': mensaje})


def dar_baja_docente(request):
    mensaje = ''
    if request.method == 'POST':
        if 'cuil' in request.POST:
            docente = get_object_or_404(Docente, cuil=request.POST['cuil'])
            docente.delete()
            mensaje = f'Operación exitosa'
    return render(request, 'persona/darBajaDocente.html', {'mensaje': mensaje})


def dar_baja_ascesor(request):
    mensaje = ''
    if request.method == 'POST':
        if 'cuil' in request.POST:
            ascesor = get_object_or_404(Ascesor, cuil=request.POST['cuil'])
            ascesor.delete()
            mensaje = f'Operación exitosa'
    return render(request, 'persona/darBajaAscesor.html', {'mensaje': mensaje})

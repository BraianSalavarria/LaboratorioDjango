from django.contrib import messages
from django.contrib.auth.models import User, Group, Permission
from django.shortcuts import render
from .forms import ComicionForm, IntegrantesComicionForm, InformeEvaluacionFormalPTFForm,TribunalForm,AsignarDocenteForm,RegistrarInformeEvTFForm
from .models import TribunalEvaluador,ComicionDeSeguimiento
from apps.proyecto.views import asignar_movimiento
from apps.proyecto.models import MovimientosPTF
from apps.persona.models import Docente
from apps.evaluacion.models import ProyectoTrabajoFinal
import logging
logger = logging.getLogger(__name__)

def registrar_comicion(request):
    nueva_comicion = None
    if request.method == 'POST':
        registrar_comicion_form = ComicionForm(request.POST)
        if registrar_comicion_form.is_valid():
            nueva_comicion = registrar_comicion_form.save(commit=True)
            messages.success(request, f'se ha registrado la comicion {nueva_comicion}')
    else:
        registrar_comicion_form = ComicionForm()
    return render(request, 'evaluacion/registroComicion.html', {'form': registrar_comicion_form})

def obtener_grupo(nombre):
    grupo = Group.objects.get(name=nombre)
    logger.debug(f'Obteniendo el grupo {grupo}')
    logger.debug(f'Sus permisos son {grupo.permissions.all()}')
    return grupo

def asignar_docente_comicion(request):
    group = obtener_grupo('comision')
    if request.method == 'POST':
        asignar_docente_comicion_form = IntegrantesComicionForm(request.POST)
        if asignar_docente_comicion_form.is_valid():
            asignar_docente_comicion_form.save(commit=True)
            docente_id = request.POST['integrante']
            comision_numero = request.POST['nroResolucioncomicion']
            logger.debug(f'Tribunal numero: {comision_numero}')
            docente = Docente.objects.get(pk=docente_id)
            comision = ComicionDeSeguimiento.objects.get(pk=comision_numero)
            logger.debug(f'El/la docente: {docente} fue agregado/a al tribunal {comision}')
            user =docente.user
            logger.debug(f'User: {user}')
            user.groups.add(group)
            user.save()
    else:
        asignar_docente_comicion_form = IntegrantesComicionForm()

    return render(request, 'evaluacion/asignaDocenteComicion.html', {'form': asignar_docente_comicion_form})


def registrar_evalucion_formal(request):
    if request.method == 'POST':
        registrar_evaluacion_formal_form = InformeEvaluacionFormalPTFForm(request.POST)
        if registrar_evaluacion_formal_form.is_valid():
            registrar_evaluacion_formal_form.save(commit=True)
            proyecto_id = request.POST['proyectoTrabajoFinal']
            proyecto =ProyectoTrabajoFinal.objects.get(pk=proyecto_id)
            asignar_movimiento('PROYECTO_EVALUADO_POR_CSTF',proyecto)
            if request.POST['estado'] == 'ACEPTADO':
                asignar_movimiento('PROYECTO_EN_EVALUACION_POR_EL_TRIBUNAL',proyecto)
    else:
        registrar_evaluacion_formal_form = InformeEvaluacionFormalPTFForm()

    return render(request, 'evaluacion/registrarInformeEvFormal.html', {'form': registrar_evaluacion_formal_form})


def registrar_tribunal(request):
    nuevo_tribunal = None
    if request.method == 'POST':
        registrar_tribunal_form = TribunalForm(request.POST)
        if registrar_tribunal_form.is_valid():
            nuevo_tribunal = registrar_tribunal_form.save(commit=True)
            messages.success(request,f'Se ha creado con exito el tribunal {nuevo_tribunal}')
    else:
        registrar_tribunal_form = TribunalForm()
    return render(request, 'evaluacion/registroTribunalEvaluador.html',{'form':registrar_tribunal_form})


def asignar_docente_tribunal(request):
    group = obtener_grupo('tribunal')
    if request.method == 'POST':
        asignar_form = AsignarDocenteForm(request.POST)
        if asignar_form.is_valid():
            asignar_form.save(commit=True)
            docente_id = request.POST['integrante']
            docente = Docente.objects.get(pk=docente_id)
            logger.debug(f'Docente: {docente}')
            user =docente.user
            user.groups.add(group)
            logger.debug(f'Grupo: {group}')
            user.save()
            logger.debug(f'User: {user}')
            logger.debug('Docente asignado con exito')
    else:
        asignar_form = AsignarDocenteForm()
    return render(request, 'evaluacion/asignaDocenteTribunal.html',{'form':asignar_form})


def registrar_evaluacion_tf(request):
    evaluacion = None
    if request.method == 'POST':
        evaluacion_form = RegistrarInformeEvTFForm(request.POST, request.FILES)
        if evaluacion_form.is_valid():
            evaluacion = evaluacion_form.save(commit=True)
            proyecto_id = request.POST['proyectoTrabajoFinal']
            proyecto =ProyectoTrabajoFinal.objects.get(pk=proyecto_id)
            asignar_movimiento('PROYECTO_EVALUADO_POR_EL_TRIBUNAL',proyecto)
            if request.POST['estado'] == 'ACEPTADO':
                asignar_movimiento('PROYECTO_APROBADO',proyecto)
            messages.success(request,f'Se ha registrado con exito la evaluacion {evaluacion}')
    else:
        evaluacion_form = RegistrarInformeEvTFForm()
    return render(request, 'evaluacion/registrarInformeEvTF.html',{'form':evaluacion_form})


def listar_tribunales(request):
    listado_tribunales = TribunalEvaluador.objects.all()
    return render(request,'evaluacion/listaTribunales.html',{'listado':listado_tribunales})


#Metodo que verifica si un proyecto tiene una determinada condicion. Devuelve true o false
def check_condicion_proyecto(proyecto,condicion):
    try:
        busqueda = MovimientosPTF.objects.filter(proyectoTrabajoFinal=proyecto,movimiento=condicion)
        return len(busqueda) > 0
    except Exception as ex:
        logger.log(ex)
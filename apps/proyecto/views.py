from django.shortcuts import render
from .forms import RegistrarProyectoTrabajoFinal,AsignarAlumnoAPTFForm,MovimientosForm
import logging
from apps.persona.models import Alumno
from apps.proyecto.models import ProyectoTrabajoFinal,IntegrantesPTF
from datetime import date
logger = logging.getLogger(__name__)


def registrar_trabajo_final(request):
    nuevo_trabajo = None
    if request.method == 'POST':
        nuevo_trabajo_form = RegistrarProyectoTrabajoFinal(request.POST,request.FILES)
        if nuevo_trabajo_form.is_valid():
            nuevo_trabajo = nuevo_trabajo_form.save(commit=True)
            logger.debug(f'se ha registrado {nuevo_trabajo}')
    else:
        nuevo_trabajo_form = RegistrarProyectoTrabajoFinal()
    return render(request, 'proyecto/registrarTF.html',{'form':nuevo_trabajo_form})


def asignar_alumno_tf(request):
    if request.method == 'POST':
        asignar_alumno_form = AsignarAlumnoAPTFForm(request.POST,request.FILES)
        if asignar_alumno_form.is_valid():
            asignar_alumno_form.save(commit=True)
            logger.debug('Se ha asignado el alumno el tf')
    else:
        asignar_alumno_form = AsignarAlumnoAPTFForm()
    return render(request, 'proyecto/asignaAlumnoTF.html',{'form':asignar_alumno_form})


def dar_baja_alumno_tf(request):
    ALUMNOS = Alumno.objects.all()
    PROYECTOS = ProyectoTrabajoFinal.objects.all()
    if request.method == 'POST':
        proyecto_id = request.POST['proyecto']
        alumno_id = request.POST['alumno']
        proyecto = IntegrantesPTF.objects.filter(proyectoTrabajoFinal=proyecto_id,integrante=alumno_id).first()
        if proyecto != None:
            proyecto.fechaBaja = date.today()
            proyecto.save()
        logger.debug(proyecto)
        
    return render(request, 'proyecto/bajaAlumnoTF.html',{'alumnos':ALUMNOS,'proyectos':PROYECTOS})


def registrar_movimiento_tf(request):
    if request.method == 'POST':
        movimiento_form = MovimientosForm(request.POST,request.FILES)
        if movimiento_form.is_valid():
            movimiento_form.save(commit=True)
            movimiento = request.POST['movimiento']
            proyecto_id = request.POST['proyectoTrabajoFinal']
            proyecto = ProyectoTrabajoFinal.objects.get(pk=proyecto_id)
            logger.debug(f'Se ha registrado el movimiento {movimiento} en el proyecto {proyecto}')
    else:
        movimiento_form = MovimientosForm()
    return render(request, 'proyecto/asignaMovimientoTF.html',{'form':movimiento_form})


def listar_tf(request):
    PROYECTOS = ProyectoTrabajoFinal.objects.all()
    return render(request, 'proyecto/listaTF.html',{'proyectos':PROYECTOS})





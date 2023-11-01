from django.shortcuts import render
from .forms import RegistrarProyectoTrabajoFinal,AsignarAlumnoAPTFForm
import logging

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
    return render(request, 'proyecto/bajaAlumnoTF.html')


def registrar_movimiento_tf(request):
    return render(request, 'proyecto/asignaMovimientoTF.html')


def listar_tf(request):
    return render(request, 'proyecto/listaTF.html')





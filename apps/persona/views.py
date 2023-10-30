from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from .forms import AlumnoForm, DocenteForm
from .models import Alumno


def registrar_alumno(request):
    nuevo_alumno = None
    if request.method == 'POST':
        registrar_alumno_form = AlumnoForm(request.POST)
        if registrar_alumno_form.is_valid():
            nuevo_alumno = registrar_alumno_form.save(commit=True)
            messages.success(request, f'se ha registrado el alumno {nuevo_alumno} correctamente')
    else:
        registrar_alumno_form = AlumnoForm()
    return render(request, 'persona/registroAlumnos.html', {'form': registrar_alumno_form})


def registrar_docente(request):
    nuevo_docente = None
    if request.method == 'POST':
        registrar_docente_form = DocenteForm(request.POST)
        if registrar_docente_form.is_valid():
            nuevo_docente = registrar_docente_form.save(commit=True)
            messages.success(request, f'se ha registrado el docente {nuevo_docente} correctamente')
    else:
        registrar_docente_form = DocenteForm()     
    return render(request, 'persona/registroDocente.html',{'form': registrar_docente_form})


def registrar_ascesor(request):
    return render(request, 'persona/registroAscesor.html')


def dar_baja_alumno(request):
    mensaje = ''
    if request.method == 'POST':
        if 'dni' in request.POST:
            alumno = get_object_or_404(Alumno, dni=request.POST['dni'])
            alumno.delete()
            mensaje = f'Operación exitosa'

    return render(request, 'persona/darBaja.html', {'mensaje': mensaje})

from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from .forms import AlumnoForm, DocenteForm, AsesorForm
from .models import Alumno, Docente, Ascesor


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
            mensaje = f'Operación exitosa'
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

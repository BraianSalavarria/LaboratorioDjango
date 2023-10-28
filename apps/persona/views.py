from django.shortcuts import render
from django.contrib import messages
from .forms import AlumnoForm


def registrar_alumno(request):
    nuevo_alumno = None
    if request.method == 'POST':
        registrar_alumno_form = AlumnoForm(request.POST)
        if registrar_alumno_form.is_valid():
            nuevo_alumno = registrar_alumno_form.save(commit=True)
            messages.success(request, 'se ha registrado correctamente')
    else:
        registrar_alumno_form = AlumnoForm()
    return render(request, 'persona/registroAlumnos.html', {'form': registrar_alumno_form})


def registrar_docente(request):
    return render(request, 'persona/registroDocente.html')


def registrar_ascesor(request):
    return render(request, 'persona/registroAscesor.html')


def dar_baja(request):

    return render(request, 'persona/darBaja.html')

from django.shortcuts import render


def registrar_alumno(request):
    return render(request, 'persona/registroAlumnos.html')


def registrar_docente(request):
    return render(request, 'persona/registroDocente.html')


def registrar_ascesor(request):
    return render(request, 'persona/registroAscesor.html')


def dar_baja(request):
    return render(request, 'persona/darBaja.html')



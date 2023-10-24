from django.shortcuts import render


def registrar_trabajo_final(request):
    return render(request, 'proyecto/registrarTF.html')


def asignar_alumno_tf(request):
    return  render(request, 'proyecto/asignaAlumnoTF.html')


def dar_baja_alumno_tf(request):
    return render(request, 'proyecto/bajaAlumnoTF.html')


def registrar_movimiento_tf(request):
    return render(request, 'proyecto/asignaMovimientoTF.html')


def listar_tf(request):
    return render(request, 'proyecto/listaTF.html')





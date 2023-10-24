from django.shortcuts import render


def registrar_comicion(request):
    return render(request, 'evaluacion/registroComicion.html')


def asignar_docente_comicion(request):
    return render(request, 'evaluacion/asignaDocenteComicion.html')


def registrar_evalucion_formal(request):
    return render(request, 'evaluacion/registrarInformeEvFormal.html')


def registrar_tribunal(request):
    return render(request, 'evaluacion/registroTribunalEvaluador.html')


def asignar_docente_tribunal(request):
    return render(request, 'evaluacion/asignaDocenteTribunal.html')


def registrar_evaluacion_tf(request):
    return render(request, 'evaluacion/registrarInformeEvTF.html')


def listar_tribunales(request):
    return render(request,'evaluacion/listaTribunales.html')

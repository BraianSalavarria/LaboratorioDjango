from django.contrib import messages
from django.shortcuts import render
from .forms import ComicionForm, IntegrantesComicionForm, InformeEvaluacionFormalPTFForm


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


def asignar_docente_comicion(request):
    if request.method == 'POST':
        asignar_docente_comicion_form = IntegrantesComicionForm(request.POST)
        if asignar_docente_comicion_form.is_valid():
            asignar_docente_comicion_form.save(commit=True)
    else:
        asignar_docente_comicion_form = IntegrantesComicionForm()

    return render(request, 'evaluacion/asignaDocenteComicion.html', {'form': asignar_docente_comicion_form})


def registrar_evalucion_formal(request):
    if request.method == 'POST':
        registrar_evaluacion_formal_form = InformeEvaluacionFormalPTFForm(request.POST)
        if registrar_evaluacion_formal_form.is_valid():
            registrar_evaluacion_formal_form.save(commit=True)
    else:
        registrar_evaluacion_formal_form = InformeEvaluacionFormalPTFForm()

    return render(request, 'evaluacion/registrarInformeEvFormal.html', {'form': registrar_evaluacion_formal_form})


def registrar_tribunal(request):
    return render(request, 'evaluacion/registroTribunalEvaluador.html')


def asignar_docente_tribunal(request):
    return render(request, 'evaluacion/asignaDocenteTribunal.html')


def registrar_evaluacion_tf(request):
    return render(request, 'evaluacion/registrarInformeEvTF.html')


def listar_tribunales(request):
    return render(request, 'evaluacion/listaTribunales.html')

from django.contrib import messages
from django.shortcuts import render
from .forms import ComicionForm,TribunalForm


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
    return render(request, 'evaluacion/asignaDocenteComicion.html')


def registrar_evaluacion_formal(request):
    return render(request, 'evaluacion/registrarInformeEvFormal.html')


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
    return render(request, 'evaluacion/asignaDocenteTribunal.html')


def registrar_evaluacion_tf(request):
    return render(request, 'evaluacion/registrarInformeEvTF.html')


def listar_tribunales(request):
    return render(request,'evaluacion/listaTribunales.html')

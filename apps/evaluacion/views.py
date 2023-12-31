from django.contrib import messages
from django.shortcuts import render
<<<<<<< HEAD
from .forms import ComicionForm, IntegrantesComicionForm, InformeEvaluacionFormalPTFForm
=======
from .forms import ComicionForm,TribunalForm,RegistrarInformeEvTFForm,AsignarDocenteForm
from .models import TribunalEvaluador
from apps.persona.models import Docente
>>>>>>> Issue-tribunal


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


<<<<<<< HEAD
def registrar_evalucion_formal(request):
    if request.method == 'POST':
        registrar_evaluacion_formal_form = InformeEvaluacionFormalPTFForm(request.POST)
        if registrar_evaluacion_formal_form.is_valid():
            registrar_evaluacion_formal_form.save(commit=True)
    else:
        registrar_evaluacion_formal_form = InformeEvaluacionFormalPTFForm()

    return render(request, 'evaluacion/registrarInformeEvFormal.html', {'form': registrar_evaluacion_formal_form})
=======
def registrar_evaluacion_formal(request):
    return render(request, 'evaluacion/registrarInformeEvFormal.html')
>>>>>>> Issue-tribunal


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
    if request.method == 'POST':
        asignar_form = AsignarDocenteForm(request.POST)
        if asignar_form.is_valid():
            asignar_form.save(commit=True)
    else:
        asignar_form = AsignarDocenteForm()
    return render(request, 'evaluacion/asignaDocenteTribunal.html',{'form':asignar_form})


def registrar_evaluacion_tf(request):
    evaluacion = None
    if request.method == 'POST':
        evaluacion_form = RegistrarInformeEvTFForm(request.POST, request.FILES)
        if evaluacion_form.is_valid():
            evaluacion = evaluacion_form.save(commit=True)
            messages.success(request,f'Se ha registrado con exito la evaluacion {evaluacion}')
    else:
        evaluacion_form = RegistrarInformeEvTFForm()
    return render(request, 'evaluacion/registrarInformeEvTF.html',{'form':evaluacion_form})


def listar_tribunales(request):
<<<<<<< HEAD
    return render(request, 'evaluacion/listaTribunales.html')
=======
    listado_tribunales = TribunalEvaluador.objects.all()
    return render(request,'evaluacion/listaTribunales.html',{'listado':listado_tribunales})
>>>>>>> Issue-tribunal

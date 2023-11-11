from django.forms import ModelForm
from .models import ComicionDeSeguimiento, IntegrantesComicion,TribunalEvaluador,IntegrantesTribunal
from apps.proyecto.models import InformeEvaluacionFormalPTF,InformeEvaluacionPTF
from django import forms


class ComicionForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["nroResolucion"].widget.attrs.update({"class": "form-control"})
        self.fields['fechaDeComicion'].widget = forms.widgets.DateInput(
            attrs={
                'type': 'date', 'placeholder': 'dd-mm-yyyy',
                'class': 'form-control'
            }
        )

    class Meta:
        model = ComicionDeSeguimiento
        fields = ('nroResolucion', 'fechaDeComicion')

    #fechaDeComicion = forms.DateInput()
        labels = {
            'nroResolucion':'Número de resolución',
            'fechaDeComicion':'Fecha de comision'
        }


class IntegrantesComicionForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['nroResolucioncomicion'].widget.attrs.update({"class": "form-control"})
        self.fields['integrante'].widget.attrs.update({"class": "form-control"})

    class Meta:
        model = IntegrantesComicion
        fields = ('nroResolucioncomicion', 'integrante')
        
        labels = {
            'nroResolucioncomicion':'Nro de resolucion de comision',
            'integrante':'Integrante'
        }


class InformeEvaluacionFormalPTFForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['observacion'].widget.attrs.update({"class": "form-control"})
        self.fields['estado'].widget.attrs.update({"class": "form-control"})
        self.fields['fechaInforme'].widget = forms.widgets.DateInput(
            attrs={
                'type': 'date', 'placeholder': 'dd-mm-yyyy',
                'class': 'form-control'
            }
        )
        self.fields['plazoObservacion'].widget = forms.widgets.DateInput(
            attrs={
                'type': 'date', 'placeholder': 'dd-mm-yyyy',
                'class': 'form-control'
            }
        )
        self.fields['comicionSeguimiento'].widget.attrs.update({"class": "form-control"})
        self.fields['proyectoTrabajoFinal'].widget.attrs.update({"class": "form-control"})

    class Meta:
        model = InformeEvaluacionFormalPTF
        fields = ('estado', 'fechaInforme', 'observacion', 'plazoObservacion','comicionSeguimiento',
                  'proyectoTrabajoFinal')
        
        labels = {
            'estado':'Estado',
            'fechaInforme':'Fecha de informe',
            'observacion':'Observacion',
            'plazoObservacion':'Plazo de observacion',
            'comicionSeguimiento':'Comision de seguimiento',
            'proyectoTrabajoFinal':'Proyecto'
        }

class TribunalForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["nroResolucion"].widget.attrs.update({"class": "form-control"})
        self.fields['fechaTribunal'].widget = forms.widgets.DateInput(
            attrs={
                'type': 'date', 'placeholder': 'dd-mm-yyyy',
                'class': 'form-control'
                }
            )

    class Meta:
        model = TribunalEvaluador
        fields = ('nroResolucion', 'fechaTribunal')
        
        labels = {
            'nroResolucion':'Nro resolucion',
            'fechaTribunal':'Fecha de tribunal'
        }
    fechaTribunal = forms.DateInput()

class AsignarDocenteForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["nroResolucionTribunal"].widget.attrs.update({"class": "form-control"})
        self.fields["integrante"].widget.attrs.update({"class": "form-control"})
        self.fields["tipo"].widget.attrs.update({"class": "form-control"})
    
    class Meta:
        model = IntegrantesTribunal
        fields = ('nroResolucionTribunal','integrante','tipo')
        
        labels = {
            'nroResolucionTribunal':'Nro resolucion',
            'integrante':'Docente',
            'tipo':'Rol'
        }

class RegistrarInformeEvTFForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["observacion"].widget.attrs.update({"class": "form-control"})
        self.fields['fechaInforme'].widget = forms.widgets.DateInput(
            attrs={
                'type': 'date', 'placeholder': 'dd-mm-yyyy',
                'class': 'form-control'
                }
            )
        self.fields["estado"].widget.attrs.update({"class": "form-control"})
        self.fields["proyectoTrabajoFinal"].widget.attrs.update({"class": "form-control"})
        self.fields["archivosAdjuntos"].widget.attrs.update({"class": "form-control"})

    class Meta:
        model = InformeEvaluacionPTF
        fields = ('observacion', 'fechaInforme','estado','proyectoTrabajoFinal','archivosAdjuntos')
        
        labels = {
            'observacion':'Observacion',
            'fechaInforme':'Fecha de informe',
            'estado':'Estado',
            'proyectoTrabajoFinal':'Proyecto',
            'archivosAdjuntos':'Archivo adjunto'
        }
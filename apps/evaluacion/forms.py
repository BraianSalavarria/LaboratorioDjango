from django.forms import ModelForm
from .models import ComicionDeSeguimiento, IntegrantesComicion, InformeEvaluacionFormalPTF,TribunalEvaluador,IntegrantesTribunal,InformeEvaluacionPTF
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

    fechaDeComicion = forms.DateInput()


class IntegrantesComicionForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['nroResolucioncomicion'].widget.attrs.update({"class": "form-control"})
        self.fields['integrante'].widget.attrs.update({"class": "form-control"})

    class Meta:
        model = IntegrantesComicion
        fields = ('nroResolucioncomicion', 'integrante')


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
        fields = ('estado', 'fechaInforme', 'observacion', 'plazoObservacion', 'comicionSeguimiento',
                  'proyectoTrabajoFinal')

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
        self.fields["tribunalElavaluador"].widget.attrs.update({"class": "form-control"})
        self.fields["proyectoTrabajoFinal"].widget.attrs.update({"class": "form-control"})
        self.fields["archivosAdjuntos"].widget.attrs.update({"class": "form-control"})

    class Meta:
        model = InformeEvaluacionPTF
        fields = ('observacion', 'fechaInforme','estado','tribunalElavaluador','proyectoTrabajoFinal','archivosAdjuntos')
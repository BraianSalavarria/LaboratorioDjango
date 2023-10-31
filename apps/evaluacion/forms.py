from django.forms import ModelForm,Form
from .models import ComicionDeSeguimiento,TribunalEvaluador, InformeEvaluacionPTF,IntegrantesTribunal
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
        
class AsignarDocenteForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["nroResolucionTribunal"].widget.attrs.update({"class": "form-control"})
        self.fields["integrante"].widget.attrs.update({"class": "form-control"})
        self.fields["tipo"].widget.attrs.update({"class": "form-control"})
        
    
    class Meta:
        model = IntegrantesTribunal
        fields = ('nroResolucionTribunal','integrante','tipo')
    
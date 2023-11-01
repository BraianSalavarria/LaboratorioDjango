from django.forms import ModelForm
from django import forms
from .models import ProyectoTrabajoFinal,IntegrantesPTF,MovimientosPTF
class RegistrarProyectoTrabajoFinal(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["titulo"].widget.attrs.update({"class": "form-control"})
        self.fields["fechaPresentacion"].widget.attrs.update({"class": "form-control"})
        self.fields["descripcion"].widget.attrs.update({"class": "form-control"})
        self.fields["NroResolucionTribunal"].widget.attrs.update({"class": "form-control"})
        self.fields["archivosAdjuntos"].widget.attrs.update({"class": "form-control"})
        self.fields["director"].widget.attrs.update({"class": "form-control"})
        self.fields["coDirector"].widget.attrs.update({"class": "form-control"})
        self.fields["ascesor"].widget.attrs.update({"class": "form-control"})
    class Meta:
        model=ProyectoTrabajoFinal
        fields = ('titulo','fechaPresentacion','descripcion','NroResolucionTribunal','archivosAdjuntos','director','coDirector'
                  ,'ascesor')
        
class AsignarAlumnoAPTFForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["proyectoTrabajoFinal"].widget.attrs.update({"class": "form-control"})
        self.fields["integrante"].widget.attrs.update({"class": "form-control"})
        self.fields["fechaAlta"].widget.attrs.update({"class": "form-control"})
        self.fields["fechaBaja"].widget.attrs.update({"class": "form-control"})
    
    class Meta:
        model = IntegrantesPTF
        fields = ('proyectoTrabajoFinal','integrante','fechaAlta','fechaBaja')
        
class MovimientosForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["movimiento"].widget.attrs.update({"class": "form-control"})
        self.fields["proyectoTrabajoFinal"].widget.attrs.update({"class": "form-control"})
        self.fields['fechaDeMovimiento'].widget = forms.widgets.DateInput(
            attrs={
                'type': 'date', 'placeholder': 'dd-mm-yyyy',
                'class': 'form-control'
                }
            )
        self.fields['fechaVencimientoMovimiento'].widget = forms.widgets.DateInput(
            attrs={
                'type': 'date', 'placeholder': 'dd-mm-yyyy',
                'class': 'form-control'
                }
            )
        self.fields["archivosAdjuntoOpcional"].widget.attrs.update({"class": "form-control"})
    
    class Meta:
        model = MovimientosPTF
        fields = ('movimiento','proyectoTrabajoFinal','fechaDeMovimiento','fechaVencimientoMovimiento','archivosAdjuntoOpcional')
    
    
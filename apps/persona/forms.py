from django.forms import ModelForm
from django import forms
from apps.persona.models import Alumno
from .models import Docente


# formulario para la clase alumno


class AlumnoForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["nombre"].widget.attrs.update({"class": "form-control"})
        self.fields["apellido"].widget.attrs.update({"class": "form-control"})
        self.fields["dni"].widget.attrs.update({"class": "form-control"})
        self.fields["matricula"].widget.attrs.update({"class": "form-control"})
        self.fields["correoElectronico"].widget.attrs.update({"class": "form-control"})
    class Meta:
        model = Alumno
        fields = ('nombre', 'apellido', 'dni', 'matricula', 'correoElectronico')
    

# formulario para la clase Docente

class DocenteForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["nombre"].widget.attrs.update({"class": "form-control"})
        self.fields["apellido"].widget.attrs.update({"class": "form-control"})
        self.fields["cuil"].widget.attrs.update({"class": "form-control"})
    class Meta:
        model = Docente
        fields = ('nombre', 'apellido', 'cuil')
        
    
        
from django.forms import ModelForm
from apps.persona.models import Alumno


# formulario para la clase alumno


class AlumnoForm(ModelForm):
    class Meta:
        model = Alumno
        fields = ('nombre', 'apellido', 'dni', 'matricula', 'correoElectronico')

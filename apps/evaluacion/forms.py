from django.forms import ModelForm
from .models import ComicionDeSeguimiento,TribunalEvaluador
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
from django import forms
from clinica.models import Dueno

class DuenoForm(forms.ModelForm):
    class Meta:
        model = Dueno
        fields = ['nombre', 'documento', 'telefono', 'direccion']
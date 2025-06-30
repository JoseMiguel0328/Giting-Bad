from django import forms
from clinica.models.bitacora_consulta import BitacoraConsulta

class BitacoraConsultaForm(forms.ModelForm):
    class Meta:
        model = BitacoraConsulta
        fields = [
            'veterinario', 'observaciones', 'diagnostico', 'tratamiento', 'medicamentos'
        ]
        widgets = {
            'observaciones': forms.Textarea(attrs={'rows': 3}),
            'diagnostico': forms.Textarea(attrs={'rows': 3}),
            'tratamiento': forms.Textarea(attrs={'rows': 3}),
            'medicamentos': forms.SelectMultiple(attrs={'class': 'form-control'}),
        }
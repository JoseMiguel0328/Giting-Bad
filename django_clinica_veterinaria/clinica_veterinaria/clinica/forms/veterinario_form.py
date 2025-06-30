from django import forms
from clinica.models.veterinario import Veterinario

class VeterinarioForm(forms.ModelForm):
    class Meta:
        model = Veterinario
        fields = ['nombre', 'documento', 'telefono', 'especialidad']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'documento': forms.TextInput(attrs={'class': 'form-control'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control'}),
            'especialidad': forms.TextInput(attrs={'class': 'form-control'}),
        }
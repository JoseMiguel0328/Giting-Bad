from django import forms
from clinica.models.cirugia import Cirugia
from clinica.models.veterinario import Veterinario

class CirugiaForm(forms.ModelForm):
    class Meta:
        model = Cirugia
        fields = ['nombre', 'descripcion', 'fecha', 'mascota', 'veterinario']
        widgets = {
            'descripcion': forms.Textarea(attrs={'class': 'form-control'}),
            'fecha': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'mascota': forms.Select(attrs={'class': 'form-control'}),
            'veterinario': forms.Select(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['veterinario'].queryset = Veterinario.objects.all()
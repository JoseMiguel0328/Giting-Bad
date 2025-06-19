# forms.py
from django import forms
from ..models import Mascota, Dueno

class MascotaForm(forms.ModelForm):
    class Meta:
        model = Mascota
        fields = '__all__'
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'especie': forms.TextInput(attrs={'class': 'form-control'}),
            'raza': forms.TextInput(attrs={'class': 'form-control'}),
            'edad': forms.NumberInput(attrs={'class': 'form-control'}),
            'dueno': forms.Select(attrs={'class': 'form-control'}),
        }

    def clean_edad(self):
        edad = self.cleaned_data['edad']
        if edad < 0:
            raise forms.ValidationError("La edad no puede ser negativa.")
        return edad

class DuenoForm(forms.ModelForm):
        class Meta:
            model = Dueno
            fields = '__all__'
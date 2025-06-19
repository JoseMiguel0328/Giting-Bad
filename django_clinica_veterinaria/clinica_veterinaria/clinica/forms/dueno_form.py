from django import forms
from ..models import Dueno

class DuenoForm(forms.ModelForm):
        class Meta:
            model = Dueno
            fields = '__all__'
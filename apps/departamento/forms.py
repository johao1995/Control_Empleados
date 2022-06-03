from django import forms
from .models import Departamento

class DepartamentoForm(forms.ModelForm):
    class Meta:
        model=Departamento
        fields=(
            'departamento',
            'area',
            'fecha'
        )
        widgets={
            'departamento':forms.TextInput(attrs={'class':'form-control','placeholder':'departamento'}),
            'area':forms.Select(attrs={'class':'form-select','placeholder':'area'}),
            'fecha':forms.DateField(attrs={'class':'form-control'})
        }
from django import forms
from .models import Empleado

class EmpleadoForm(forms.ModelForm):
    class Meta:
        model=Empleado
        fields=(
            'first_name',
            'last_name',
            'puesto',
            'codigo_departamento',
            'habilidad',
            'image',
            'fecha'
        )
        widgets={
            'first_name':forms.TextInput(attrs={'class':'form-control','placeholder':'first name'}),
            'last_name':forms.TextInput(attrs={'class':'form-control','placeholder':'last name'}),
            'puesto':forms.TextInput(attrs={'class':'form-control','placeholder':'first name'}),
            'codigo_departamento':forms.Select(attrs={'class':'form-select'}),
            'habilidad':forms.SelectMultiple(attrs={'class':'form-control'}),
            'image':forms.FileInput(attrs={'class':'form-control'}),
            'fecha':forms.DateInput(attrs={'class':'form-control','type':'date'})
        }

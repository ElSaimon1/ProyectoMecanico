from django.forms import ModelForm
from django import forms
from .models import Tipo_servicio, Comuna, Formulario

class CrearRegistro(ModelForm):
    class Meta:
        model = Formulario
        fields = ['patente','marca','modelo','telefono','tipo_ser','comuna','Detalles_servicio']
        widgets = {
            'patente': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ejem: 2D8W6G'}),
            'marca': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ejem: Mercedes'}),
            'modelo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ejem: VDH-54'}),
            'telefono': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Ejem: +56 999 666 333'}),
            'tipo_ser': forms.Select(attrs={'class': 'form-control'}),
            'comuna': forms.Select(attrs={'class': 'form-control'}),
            'Detalles_servicio': forms.Textarea(attrs={'class': 'form-control'}),
        }

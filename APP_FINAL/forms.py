from django import forms
from .models import models_inscritos,models_instituciones



class formu_inscritos(forms.ModelForm):
    class Meta:
        model = models_inscritos
        fields = ['nombre','telefono','institucion','estado','observacion']
        widgets ={
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'telefono': forms.NumberInput(attrs={'class': 'form-control'}),
           
            'institucion': forms.Select(attrs={'class': 'form-select'}),
            'estado': forms.Select(attrs={'class': 'form-select'}),
            'observacion':forms.Textarea(attrs={'class': 'form-control'})
        }

class formu_instituciones(forms.ModelForm):
    class Meta:
        model = models_instituciones
        fields = ['nombre']
        widgets ={
            'nombre': forms.TextInput(attrs={'class': 'form-control'})
        }
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django import forms
from aplicaciones.mascota.models import Mascota


class MascotaForm(forms.ModelForm):
    
    class Meta:
        model = Mascota

        fields = [
            'nombre',
            'sexo',
            'edad_aprox',
            'fecha_rescate',
            'persona',
            'vacuna',
            'imagen'
        ]
        labels = {
            'nombre': 'Nombre',
            'sexo': 'Sexo',
            'edad_aprox': 'Edad aproximada',
            'fecha_rescate': 'Fecha de rescate (YYYY-MM-DD)',
            'persona': 'Adoptante',
            'vacuna': 'Vacunas',
            'imagen': 'Fotografía'
        }
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'sexo': forms.TextInput(attrs={'class': 'form-control'}),
            'edad_aprox': forms.TextInput(attrs={'class': 'form-control'}),
            'fecha_rescate': forms.TextInput(attrs={'class': 'form-control'}),
            'persona': forms.Select(attrs={'class': 'form-control'}),
            'vacuna': forms.CheckboxSelectMultiple(),
            
        }
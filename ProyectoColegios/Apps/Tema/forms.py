
# -*- coding: utf-8 -*-
from django import forms
from Apps.Estudiantes.models import Estudiante

__author__      = "Luis David Montoya Diaz"
__copyright__   = "Copyright 2018, ISUC"

class FormCrearEstudiante(forms.ModelForm):
	class Meta:
		model = Estudiante
		fields = [
			'codigo',
			'nombre',
			'apellido',
			'sexo',
			'edad',
			'email',
			'direccion',

		]

		labels = {

            'codigo':'Codigo',
            'nombre':'Nombre',
            'apellido':'Apellido',
            'sexo':'Sexo',
            'edad':'Edad',
            'email':'E-mail',
            'direccion':'Dirección',

		}

		widgets = {
			'codigo': forms.NumberInput(attrs={'class': 'form-control'}),
			'nombre': forms.TextInput(attrs={'class': 'form-control'}),
			'apellido': forms.TextInput(attrs={'class': 'form-control'}),
            'sexo': forms.TextInput(attrs={'class': 'form-control'}),
            'edad': forms.NumberInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control'}),
        }


class FormActualizarEstudiante(forms.ModelForm):
	class Meta:
		model = Estudiante
		fields = [
			'codigo',
			'nombre',
			'apellido',
			'sexo',
			'edad',
			'email',
			'direccion',

		]

		labels = {

			'codigo': 'Codigo',
			'nombre': 'Nombre',
			'apellido': 'Apellido',
			'sexo': 'Sexo',
			'edad': 'Edad',
			'email': 'E-mail',
			'direccion': 'Dirección',

		}

		widgets = {
			'codigo': forms.NumberInput(attrs={'readonly':'readonly','class': 'form-control'}),
			'nombre': forms.TextInput(attrs={'class': 'form-control'}),
			'apellido': forms.TextInput(attrs={'class': 'form-control'}),
			'sexo': forms.TextInput(attrs={'class': 'form-control'}),
			'edad': forms.NumberInput(attrs={'class': 'form-control'}),
			'email': forms.EmailInput(attrs={'class': 'form-control'}),
			'direccion': forms.TextInput(attrs={'class': 'form-control'}),
		}


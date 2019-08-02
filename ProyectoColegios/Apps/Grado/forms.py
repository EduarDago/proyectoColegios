
# -*- coding: utf-8 -*-
from django import forms
from Apps.Estudiantes.models import Estudiante

__author__      = "Nodier Jose Pineda Villa"
__copyright__   = "Copyright 2018, INSUC"

class FormCrearGrado(forms.ModelForm):
	class Meta:
		model = Grado
		fields = [
		'idGrado',
			
		]

		labels = {

		'idGrado':'Codigo del grado',
		
		
		}

		widgets = {

		'idGrado': forms.TextInput(attrs={'class': 'form-control'}),
		
				
		}

#actualizar grado
class FormActualizarGrado(forms.ModelForm):
	class Meta:
		model = Grado
		fields = [
		'idGrado',
			
		]

		labels = {

		'idGrado':'Codigo del grado',
		
		
		}

		widgets = {

		'idGrado': forms.TextInput(attrs={'class': 'form-control'}),
		
				
		}
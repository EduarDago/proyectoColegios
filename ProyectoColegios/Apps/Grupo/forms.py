
# -*- coding: utf-8 -*-
from django import forms
from Apps.Estudiantes.models import Estudiante

__author__      = "Nodier Jose Pineda Villa"
__copyright__   = "Copyright 2018, INSUC"

class FormCrearGrupo(forms.ModelForm):
	class Meta:
		model = Grupo
		fields = [
		'idGrupo',	
		'foraneaGrado'
		]

		labels = {
		'idGrupo':'Codigo del grupo',
		'foraneaGrado':'asignar el grado'		
		}

		widgets = {
		'idGrupo': forms.TextInput(attrs={'class': 'form-control'}),
		'foraneaGrado': forms.Select(attrs={'class':'mdb-select colorful-select dropdown-ins'}),
		}
		

#actualizar grado
class FormActualizarGrupo(forms.ModelForm):
	class Meta:
		model = Grupo
		fields = [
		'idGrupo',	
		'foraneaGrado'
		]

		labels = {
		'idGrupo':'Codigo del grupo',
		'foraneaGrado':'asignar el grado'		
		}

		widgets = {
		'idGrupo': forms.TextInput(attrs={'class': 'form-control'}),
		'foraneaGrado': forms.Select(attrs={'class':'mdb-select colorful-select dropdown-ins'}),
		}





		
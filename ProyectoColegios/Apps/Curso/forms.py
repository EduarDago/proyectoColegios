
__author__      = "Juan Pablo Aguirre Chica"
__copyright__   = "Copyright 2018, ISUC"

from django import forms
from Apps.Curso.models import Curso


class FormCrearCurso(forms.ModelForm):
	class Meta:
		model = Curso
		fields = [
			'idCurso',	
			'foraneaMateriaGrado',
			'foraneaProfesor',
			'foraneaGrupo',
		]

		labels = {

			'idCurso':'codigo del curso',
			'foraneaMateriaGrado':'Materia', 
			'foraneaProfesor':'profesor asignado',	
			'foraneaGrupo':'grupo',        

		}

		widgets = {
			'idCurso': forms.TextInput(attrs={'class': 'form-control'}),
			'foraneaMateriaGrado': forms.Select(attrs={'class': 'mdb-select colorful-select dropdown-ins'}),
			'foraneaProfesor': forms.Select(attrs={'class': 'mdb-select colorful-select dropdown-ins'}),
			'foraneaGrupo': forms.Select(attrs={'class': 'mdb-select colorful-select dropdown-ins'}),
		}

class FormActualizarCurso(forms.ModelForm):
	class Meta:
		model = Curso
		fields = [
			'idCurso',	
			'foraneaMateriaGrado',
			'foraneaProfesor',
			'foraneaGrupo',
		]

		labels = {

			'idCurso':'codigo del curso',
			'foraneaMateriaGrado':'Materia', 
			'foraneaProfesor':'profesor asignado',	
			'foraneaGrupo':'grupo',        

		}

		widgets = {
			'idCurso': forms.TextInput(attrs={'class': 'form-control'}),
			'foraneaMateriaGrado': forms.Select(attrs={'class': 'mdb-select colorful-select dropdown-ins'}),
			'foraneaProfesor': forms.Select(attrs={'class': 'mdb-select colorful-select dropdown-ins'}),
			'foraneaGrupo': forms.Select(attrs={'class': 'mdb-select colorful-select dropdown-ins'}),
		}

#coding=utf-8
from django import forms
from Apps.Materia.models import Materia

#formulario para crear materia
class FormCrearMateria(forms.ModelForm):
	class Meta:
		model = Materia
		fields = [
		'id',
		'nombre',
		'intensidad',
		]

		labels = {
		'id': 'Identificación',
		'nombre': 'Nombre',
		'intensidad': 'Intensidad horaria',
		}

		widgets = {
		'id': forms.TextInput(attrs={'class': 'form-control'}),
		'nombre': forms.TextInput(attrs={'class': 'form-control'}),
		'intensidad': forms.TextInput(attrs={'class': 'form-control'}),
		}

#formulario para crear materia
class FormActualizarMateria(forms.ModelForm):
	class Meta:
		model = Materia
		fields = [
		'id',
		'nombre',
		'intensidad',
		]

		labels = {
		'id': 'Identificación',
		'nombre': 'Nombre',
		'intensidad': 'Intensidad horaria',
		}

		widgets = {
		'id': forms.TextInput(attrs={'readonly':'readonly', 'class': 'form-control form-control-sm'}),
		'nombre': forms.TextInput(attrs={'class': 'form-control form-control-sm'}),
		'intensidad': forms.TextInput(attrs={'class': 'form-control form-control-sm'}),
		}


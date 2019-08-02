
# -*- coding: utf-8 -*-
from django import forms
from Apps.Tarea.models import Tarea

__author__      = "Luis David Montoya Diaz"
__copyright__   = "Copyright 2018, ISUC"

class FormCrearTarea(forms.ModelForm):
	
	#check = forms.BooleanField()	
	#idEstudiante = forms.CharField(widget=forms.HiddenInput())
	
	class Meta:
		model = Tarea
		fields = [

			'idTarea',
			'tituloTarea',
			'descripcionTarea',
			'fechaLimite',
			'rutaArchivo',
			'logrosTarea',
			'foraneaTema',
			'foraneaCurso',
			#'check',
			#'idEstudiante'

		]

		labels = {

			'idTarea': 'codigo de la tarea',
			'tituloTarea': 'Título de la tarea' ,
			'descripcionTarea': 'Descripción de la tarea',
			'fechaLimite': 'Fecha limite de entrega',
			'rutaArchivo': 'Adjuntar archivo',
			'logrosTarea': 'Logros',
			'foraneaTema': 'Tema',
			'foraneaCurso': 'Curso'
            
		}

		widgets = {

			'idTarea': forms.TextInput(attrs={'class': 'form-control'}),
			'tituloTarea': forms.TextInput(attrs={'class': 'form-control'}),
			'descripcionTarea':forms.Textarea (attrs={'class': 'form-control'}),
			'fechaLimite': forms.TextInput(attrs={'class': 'form-control datetimepicker-input', 'data-target':'#datetimepicker1'}),
			'logrosTarea': forms.Textarea(attrs={'class': 'md-textarea form-control'}),			
			'foraneaTema': forms.TextInput(attrs={'class':'form-control'}),
			'foraneaCurso': forms.TextInput(attrs={'class':'form-control'})
   	}
		

	#Una forma de hacer validaciones cuando se envia el formulario

	#Una forma de hacer validaciones

	def clean(self):
		tituloTarea = self.cleaned_data.get("tituloTarea")
		foraneaCurso = self.cleaned_data.get("foraneaCurso")
		#print('-----------',tituloTarea, fechaLimite, foraneaCurso)
		if ( self.ExisteTareaEnCurso(tituloTarea, foraneaCurso)):
		#if ( tituloTarea == 'tutulo2' ):
			self.add_error('tituloTarea', 'Título ya existente. El título no puede estar mas de una vez')
		#print("........ ",tituloTarea)
		
	
	def ExisteTareaEnCurso(self,titulo,curso):
		temporal = Tarea.objects.filter(tituloTarea=titulo,foraneaCurso=curso)
		return temporal.exists()


						
						
class FormActualizarTarea(forms.ModelForm):
	class Meta:
		model = Tarea
		fields = [

			'idTarea',
			'tituloTarea',
			'descripcionTarea',
			'fechaLimite',
			'rutaArchivo',
			'logrosTarea',
			'foraneaCurso',

		]

		labels = {

			'idTarea': 'codigo de la tarea',
			'tituloTarea': 'título de la tarea' ,
			'descripcionTarea': 'descripcion de la tarea',
			'fechaLimite': 'fecha limite de la tarea',
			'rutaArchivo': 'adjuntar archivo',
			'logrosTarea': 'Logros',
			'foraneaCurso': 'curso',
            
		}

		widgets = {

			'idTarea': forms.TextInput(attrs={'class': 'form-control'}),
			'tituloTarea': forms.TextInput(attrs={'class': 'form-control'}),
			'descripcionTarea': forms.Textarea(attrs={'class': 'form-control'}),
			'fechaLimite': forms.DateTimeInput(format=['%Y/%m/%d %H:%M'], attrs={'class': 'form-control'}),
			#'rutaArchivo': forms.FileField(), no se puede modificar el porque viene desde el modelo
			'logrosTarea': forms.Textarea(attrs={'class': 'form-control'}),
			'foraneaCurso': forms.TextInput(attrs={'class':'mdb-select colorful-select dropdown-ins'}),
		}
		
		


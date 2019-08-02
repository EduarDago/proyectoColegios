
from django import forms
from Apps.Estudiante.models import Estudiante, Actividad

__author__      = "Luis David Montoya Diaz"
__copyright__   = "Copyright 2018, ISUC"

class FormCrearEstudiante(forms.ModelForm):
	
	class Meta:
		model = Estudiante
		fields = [
		'codigo',
		'sexo',
		'edad',
		'email',
		'direccion',
		'foraneaGrupo',
		]

		labels = {

		'codigo':'Codigo',
		'sexo':'Sexo',
		'edad':'Edad',
		'email':'E-mail',
		'direccion':'Dirección',
		'foraneaGrupo' : 'Asociar al grupo'

		}


		widgets = {

		'codigo': forms.TextInput(attrs={'class': 'form-control'}),
		'sexo': forms.TextInput(attrs={'class': 'form-control'}),
		'edad': forms.NumberInput(attrs={'class': 'form-control'}),
		'email': forms.TextInput(attrs={'class': 'form-control'}),
		'direccion': forms.TextInput(attrs={'class': 'form-control'}),
		'foraneaGrupo' : forms.Select(attrs={'class':'mdb-select colorful-select dropdown-ins'}),


		}


#actualizar estudiante
class FormActualizarEstudiante(forms.ModelForm):
	class Meta:
		model = Estudiante
		fields = [
		'codigo',
		'sexo',
		'edad',
		'email',
		'direccion',
		'foraneaGrupo',
		]

		labels = {

		'codigo':'Codigo',
		'sexo':'Sexo',
		'edad':'Edad',
		'email':'E-mail',
		'direccion':'Dirección',
		'foraneaGrupo' : 'Asociar al grupo'

		}


		widgets = {

		'codigo': forms.TextInput(attrs={'class': 'form-control'}),
		'sexo': forms.TextInput(attrs={'class': 'form-control'}),
		'edad': forms.NumberInput(attrs={'class': 'form-control'}),
		'email': forms.TextInput(attrs={'class': 'form-control'}),
		'direccion': forms.TextInput(attrs={'class': 'form-control'}),
		'foraneaGrupo' : forms.Select(attrs={'class':'mdb-select colorful-select dropdown-ins'}),


		}
		
		
		
class FormCrearActividad(forms.ModelForm):
	class Meta:
		model = Actividad
		fields = [
			
			'tituloActividad',
			'descripcionActividad',
			'estado',
			'rutaArchivo',
			'foraneaMateriaGrado', 
			'foraneaEstudiante'

		]

		labels = {
			
			'tituloActividad' : 'Título de la actividad',
			'descripcionActividad' : 'Descripción de la actividad',
			'estado' : 'Estado de la tarea',
			'rutaArchivo' : 'adjuntar archivo',
			'foraneaMateriaGrado' : 'Materia del Grado',
			'foraneaEstudiante' : 'Estudiante'

		}

		widgets = {
			'tituloActividad': forms.TextInput(attrs={'class': 'form-control'}),
			'descripcionActividad': forms.Textarea(attrs={'class': 'form-control','id':'id_descripcionTarea'}),
			'estado': forms.Textarea(attrs={'class': 'form-control'}),
			'foraneaMateriaGrado': forms.TextInput(attrs={'class':'form-control'}),
			'foraneaEstudiante' : forms.TextInput(attrs={'class':'form-control'}),
		}
		
	def clean(self):
		tituloActividad = self.cleaned_data.get("tituloActividad")
		#print('-----------',tituloTarea, fechaLimite, foraneaCurso)
		if ( self.ExisteActividad(tituloActividad)):
		#if ( tituloTarea == 'tutulo2' ):
			self.add_error('tituloActividad', 'Título ya existente. El título no puede estar mas de una vez')
		#print("........ ",tituloTarea)


	def ExisteActividad(self,titulo):
		temporal = Actividad.objects.filter(tituloActividad=titulo)
		return temporal.exists()


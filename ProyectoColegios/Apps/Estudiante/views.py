__author__      = "Luis David Montoya Diaz"
__copyright__   = "Copyright 2018, ISUC"

from django.shortcuts import render
from django.http import HttpResponse, request
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, ListView, DeleteView
from django.views.generic import TemplateView
from django.http.response import HttpResponseRedirect

from Apps.Estudiante.models import Estudiante, Actividad
from Apps.Estudiante.forms import FormCrearEstudiante,FormActualizarEstudiante, FormCrearActividad



class CrearEstudiante(CreateView):
	model = Estudiante
	form_class = FormCrearEstudiante
	template_name = 'CrearEstudiante.html'
	success_url=reverse_lazy('index')


class ActualizarEstudiante(UpdateView):
	model=Estudiante
	form_class=FormActualizarEstudiante
	template_name='ActualizarEstudiante.html'
	success_url = reverse_lazy('ConsultarEstudiante')

class EliminarEstudiante(DeleteView):
	model = Estudiante
	template_name = 'EliminarEstudiante.html'
	success_message='estudiante eliminada exitosamente.'


class ConsultarEstudiante(ListView):
	model = Estudiante
	template_name = 'ConsultarEstudiante.html'


#Actividades

class CrearActividad(CreateView):
	model = Actividad
	form_class = FormCrearActividad
	template_name = 'CrearActividad.html'
	
	def get(self, request, *args, **kwargs):
		codigoEstudiante = self.kwargs['pk'] # forma de obtener el id
		#obtener las materia del curso al cual se encuantra vinculado el estudiante
		materiaGrado = cargarMateriasEstudiante(codigoEstudiante)
		#print(materiaGrado)
		self.object = None
		form_class = self.get_form_class()
		form = self.get_form(form_class)
		return self.render_to_response(self.get_context_data(form=form, materiaGrado=materiaGrado, codigoEstudiante = codigoEstudiante))
	
	def post(self, request, *args, **kwargs):
		self.object = None
		form_class = self.get_form_class()
		form = self.get_form(form_class)
		#datos = request.POST.get('tabla')
		
		form = FormCrearActividad(request.POST, request.FILES)
		idCurso = self.kwargs['pk']
		if ( form.is_valid()):
			form.save()
			#agregarTareasEstudiantes(form['idTarea'])
			
			return HttpResponseRedirect(reverse_lazy('GUIGestionContenidoCurso'));
		else:
			codigoEstudiante = self.kwargs['pk'] # forma de obtener el id
			#obtener las materia del curso al cual se encuantra vinculado el estudiante
			materiaGrado = cargarMateriasEstudiante(codigoEstudiante)
			return self.render_to_response(self.get_context_data(form=form, materiaGrado=materiaGrado, codigoEstudiante = codigoEstudiante))
	
	
""" 
	Función que busca un estudiante en la base de datos y
	lo retorna como un objeto de la clase Estudiante.
	 
	
	Parametros:

	codigoEstudiante -- codigo del estudiante a buscar.
	
"""

def BuscarEstudiante(codigoEstudiante):

	estudiante=Estudiante.objects.get(codigo=codigoEstudiante)
	return estudiante


""" 
	Función carga todas las tareas de los estudiantes en la base de datos y
	las retorna como un objeto de la clase Tarea.
	 
	
	Parametros:

	codigoEstudiante -- codigo del estudiante al cual se le asignaron las tareas.
	
"""
def cargarTareasdeEstudiante(codigoEstudiante):
	estudiante=BuscarEstudiante(codigoEstudiante)
	tareas=estudiante.tareasEstudiante.all()
	return tareas
	#return self.render_to_response(self.get_context_data(form=form, temasCurso=temasCurso, estudiantesCurso=estudiantesCurso, idCurso=idCurso))

	
	
	
def cargarMateriasEstudiante(codigoEstudiante):
	estudiante = BuscarEstudiante(codigoEstudiante)
	grado = estudiante.foraneaGrupo
	grupo = grado.foraneaGrado
	cursos = grupo.materiagrado_set.all()
	
	return cursos
	




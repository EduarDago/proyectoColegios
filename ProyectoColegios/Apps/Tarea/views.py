# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import messages
from django.shortcuts import render, get_object_or_404 
from django.views.generic import CreateView, UpdateView, ListView, DeleteView, DetailView
from django.urls import reverse_lazy
from django.http.response import HttpResponseRedirect

from Apps.Estudiante.views import cargarTareasdeEstudiante
from Apps.MateriaGrado.views import cargarTemasTarea
from Apps.Curso.views import cargarEstudiantesCurso

from Apps.Tarea.filetransfers.api import prepare_upload, serve_file
from Apps.Tarea.models import Tarea
from Apps.Tarea.forms import FormCrearTarea




# Create your views here.

#Listar Materia
class ConsultarTarea(DetailView):
	model = Tarea
	template_name = 'ConsultarTarea.html'
	
'''class ConsultarTodasTareas(ListView):
	model = Tarea
	template_name = 'ConsultarTodasTareas.html'''

def ConsultarTodasTareas(request,codigoEstudiante):
	tareas=cargarTareasdeEstudiante(codigoEstudiante)
	return render(request, 'ConsultarTodasTareas.html', {'tareas': tareas})

def descargarArchivo(request, pk):
	tarea = get_object_or_404(Tarea, pk = pk )
	return serve_file(request, tarea.rutaArchivo, save_as = True)

def agregarTareasEstudiantes(self,idTarea):
	
	tarea = Tareas.objects.get(idTarea = idTarea)
	curso = tarea.foraneaCurso
	grupo = curso.foraneaGrupo
	estudiantes = grupo.estudiante_set.all()

	for estudiante in estudiantes:
		estudiante.tareasEstudiante.add(tarea)
	
class CrearTarea(CreateView):
	model = Tarea
	form_class = FormCrearTarea
	template_name = 'CrearTarea.html'
	
	def get(self, request, *args, **kwargs):
		idCurso = self.kwargs['idCurso'] # forma de obtener el id
		temasCurso = cargarTemasTarea(idCurso)
		estudiantesCurso = cargarEstudiantesCurso(idCurso)
		self.object = None
		form_class = self.get_form_class()
		form = self.get_form(form_class)
		return self.render_to_response(self.get_context_data(form=form, temasCurso=temasCurso, estudiantesCurso = estudiantesCurso, idCurso = idCurso))
	
	def post(self, request, *args, **kwargs):
		self.object = None
		form_class = self.get_form_class()
		form = self.get_form(form_class)
		idCurso = self.kwargs['idCurso']
		Datos=cargarEstudiantesCurso(idCurso)
		for est in Datos:
			ref=str(est.codigo)
			seleccionado = request.POST.get(ref)
		#datos2 = request.POST.get('1')
			print('------------->',seleccionado)
		#print(form['fechaLimite'])
		form = FormCrearTarea(request.POST, request.FILES)

		#print("0000",form['tituloTarea'],form['foraneaCurso'])
		if ( form.is_valid()):
			form.save()
			#agregarTareasEstudiantes(form['idTarea'])
			idCurso = self.kwargs['idCurso']
			return HttpResponseRedirect(reverse_lazy('GUIGestionContenidoCurso', kwargs={'idCurso': idCurso} ))
		else:
			idCurso = self.kwargs['idCurso'] # forma de obtener el id
			temasCurso = cargarTemasTarea(idCurso)
			estudiantesCurso = cargarEstudiantesCurso(idCurso)
			return self.render_to_response(self.get_context_data(form=form, temasCurso=temasCurso, estudiantesCurso = estudiantesCurso, idCurso = idCurso))

	




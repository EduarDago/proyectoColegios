# -*- coding: utf-8 -*-

__author__      = "Juan Pablo Aguirre Chica"
__copyright__   = "Copyright 2018, ISUC"

from django.shortcuts import render
from django.db.models import Count
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, ListView, DeleteView

from Apps.Curso.models import Curso
from Apps.MateriaGrado.models import MateriaGrado
from Apps.Curso.forms import FormCrearCurso, FormActualizarCurso





# Create your views here.
class CrearCurso(CreateView):
	model = Curso
	form_class = FormCrearCurso
	template_name = 'CrearCurso.html'
	success_url=reverse_lazy('ConsultarCurso')
#crea la vista de consultar cursos
class ConsultarCurso(ListView):
	model = Curso
	template_name = 'ConsultarCurso.html'
#crea la vista de actualizar cursos
class ActualizarCurso(UpdateView):
	model=Curso
	form_class= FormActualizarCurso
	template_name='ActualizarCurso.html'
	success_url = reverse_lazy('ConsultarCurso')
#crea la vista de eliminar cursos
class EliminarCurso(DeleteView):
	model = Curso
	template_name = 'EliminarCurso.html'
	success_message='Curso eliminado exitosamente.'
	success_url=reverse_lazy('ConsultarCurso')

def mostrarContenidoCurso(request,idCurso):
	'''Este metodo retorna un conjunto con idtarea,tituloTarea,fechaLimite segun el idCurso que se recibe por parametro'''
	curso=buscarCurso(idCurso)
	tareas=buscarTareasCurso(curso)
	return render(request, 'GUIGestionContenidoCurso.html', {'tareas': tareas, 'idCurso':idCurso})

def buscarCurso(idCurso):
		curso=Curso.objects.get(idCurso=(int(idCurso)))
		return curso


def buscarTareasCurso(curso):
	tareas = curso.tarea_set.all()
	return tareas

def cargarEstudiantesCurso(idCurso):
	curso = buscarCurso(idCurso)
	grupo = curso.foraneaGrupo
	estudiantes = grupo.estudiante_set.all()
	return estudiantes

	
#def cargarTemasCurso(idCurso):
	#'''Este metodo retorna un conjunto con el idTema y el nombre del tema'''
	#curso=buscarCurso(idCurso)
	#temas=curso.tema.all()
	#return temas


def materiasCursosProfesor(id):
		#'SELECT C.foraneaMateriaGrado_id FROM curso_curso AS C WHERE C.foraneaProfesor_id = 2 GROUP BY C.foraneaMateriaGrado_id'
		materias = Curso.objects.values('foraneaMateriaGrado').filter(foraneaProfesor = id).annotate(dcount=Count('foraneaMateriaGrado'))
		vector = []
		for materia in materias:
			tupla = {}
			foraneaMateriaGrado = materia['foraneaMateriaGrado']
			tupla['materia'] = MateriaGrado.objects.get(idMateriaGrado = foraneaMateriaGrado)
			tupla['cursos'] = Curso.objects.filter(foraneaMateriaGrado = foraneaMateriaGrado)
			vector.append(tupla)
			
		return vector

#Método encarcado de validar si el cusrso existe
def validarObjetoExiste(idCurso):
	
	if Entry.objects.filter(idCurso = (int(idCurso))):
		return True
	
	return False



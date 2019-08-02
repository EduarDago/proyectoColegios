# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic import CreateView, UpdateView, ListView, DeleteView
from Apps.Materia.models import Materia
from Apps.Materia.forms import FormCrearMateria, FormActualizarMateria


from django.urls import reverse_lazy

class CrearMateria(CreateView):
	model = Materia
	form_class = FormCrearMateria
	template_name = 'CrearMateria.html'
	success_url=reverse_lazy('ConsultarMateria')

# vista actualizacion materia
class ActualizarMateria(UpdateView):
	model = Materia
	form_class = FormActualizarMateria
	template_name = 'ActualizarMateria.html'
	success_url=reverse_lazy('ConsultarMateria')

# vista listar materia
class ListarMaterias(ListView):
	model = Materia
	template_name = 'ListarMaterias.html'

#vista eliminar materia
class EliminarMateria(DeleteView):
	model = Materia
	template_name = 'EliminarMateria.html'
	success_message='materia eliminada exitosamente.'
	success_url=reverse_lazy('ConsultarMateria')


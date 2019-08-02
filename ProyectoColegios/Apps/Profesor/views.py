# -*- coding: utf-8 -*-
# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.views.generic import CreateView, TemplateView
from django.urls import reverse_lazy
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.core.exceptions import ObjectDoesNotExist
from Apps.Profesor.models import Profesor
from Apps.Profesor.forms import formProfesor



__author__      = "Eduard"
__copyright__   = "Copyright 2018, ISUC"

class CrearProfesor(CreateView):
	model = Profesor
	form_class = formProfesor
	template_name='CrearProfesor.html'
	success_url=reverse_lazy('index')


	
	'''
	def form_valid(self, form):
		''
		En este parte, si el formulario es valido guardamos lo que se obtiene de él y usamos authenticate para que el usuario incie sesión luego de haberse registrado y lo redirigimos al index
		'
		instance = profile_form.save(commit=False)
    instance.user = request.user
    instance.save()
		print(form)
		form.save()
		usuario = form.cleaned_data.get('username')
		password = form.cleaned_data.get('password1')
		#usuario = authenticate(username=usuario, password=password)
		#login(self.request, usuario)
		return redirect('index')
		'''





def buscarProfesor(codigoprofesor):
	try:
		profe=Profesor.objects.get(codigoprofesor=(int(codigoprofesor)))
		return profe,True
	except(ObjectDoesNotExist):
		mensaje=("El profesor con codigo"+str(codigoprofesor)+"no existe")
		return mensaje,False

def cargarCursosProfesor(request,codigoProfesor):
	'''Este metodo retorna los cursos asociados al profesor, retorna el id del curso,
	la materia y el grado, si el profesor no existe retorna un mensaje'''

	profesor,error=buscarProfesor(codigoProfesor)
	if error:
		cursos=profesor.curso_set.all()
		return render(request, 'ActualizarProfesor.html', {'cursos': cursos}) # se debe editar el template
	else:
		return render(request, 'ActualizarProfesor.html', {'cursos': profesor})








	

from Apps.Grado.models import Grado

__author__ = "Luis David Montoya Diaz"
__copyright__ = "Copyright 2018, ISUC"
# -*- coding: utf-8 -*-

from django.contrib.auth.models import User
from django.db import models
from Apps.Grupo.models import Grupo
from Apps.Tarea.models import Tarea
from Apps.MateriaGrado.models import MateriaGrado

# Create your models here.
"""
	Clase que define el modelo Estudiante
	
	Parámetros:

    usuarioEstudiante -- se crea una asociacion en la base de datos entre la tabla User( creada por defecto por Django) y 
						 la tabla Estudiante
    codigo -- código del estudiante.
    sexo -- sexo del estudiante.
	edad -- edad del estudiante.
	email -- correo electronico del estudiante.
	direccion -- direccion de residencia del estudiante
	foraneaGrupo = identificador del modelo Grupo asociado al estudiante
	tareasEstudiante = se crea una relacion 'Many To Many' en la base de datos entre la tabla Tarea y 
						 la tabla Estudiante

"""

class Estudiante(models.Model):
	usuarioEstudiante = models.OneToOneField(User, on_delete=models.CASCADE)
	codigo = models.CharField(primary_key=True, max_length=40)
	sexo = models.CharField(max_length=20)
	edad = models.PositiveIntegerField()
	email = models.CharField(max_length=70)
	direccion = models.CharField(max_length=70)
	foraneaGrupo = models.ForeignKey(Grupo, null=True,blank=True, on_delete=models.CASCADE)
	tareasEstudiante = models.ManyToManyField(Tarea)

	""" 
		Función que permite retornar al modelo o vista asociada a un estudiante, 
		su nombre de usuario respectivo
	
	"""
	def __str__(self):
		return '{}'.format(self.usuarioEstudiante.username)

	
class Actividad(models.Model):
	idActividad = models.AutoField(primary_key=True, max_length=10)
	tituloActividad=models.CharField(max_length=70)
	descripcionActividad=models.TextField(max_length=200)
	estado=models.BooleanField()#organizar a boolean
	rutaArchivo=models.FileField(upload_to='Archivos/Actividad/', null=True, blank=True)#organizar upload to
	calificacion=models.PositiveIntegerField(default=0)	
	foraneaMateriaGrado=models.ForeignKey(MateriaGrado,on_delete=models.CASCADE)
	foraneaEstudiante=models.ForeignKey(Estudiante,null=True,blank=True, on_delete=models.CASCADE)

	def __str__(self):
		return '{}'.format(self.tituloActividad)
	
	@property
	def filename(self):
		return self.rutaArchivo.name.rsplit('/', 1)[-1]



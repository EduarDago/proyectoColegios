# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from datetime import datetime

from django.db import models


from Apps.Curso.models import Curso
from Apps.Tema.models import Tema
from Apps.MateriaGrado.models import MateriaGrado

# Create your models here.
class Tarea(models.Model):
	
	idTarea = models.AutoField(primary_key=True, max_length=10)
	tituloTarea = models.CharField(max_length=50)
	descripcionTarea = models.TextField(max_length=200)
	fechaLimite = models.DateTimeField(default=datetime.now)
	rutaArchivo = models.FileField(upload_to='Tarea/Profesor/', null=True, blank=True)
	logrosTarea = models.TextField(max_length=200, null=True, blank=True)
	foraneaCurso = models.ForeignKey(Curso, null=True, blank=True, on_delete=models.CASCADE)
	foraneaTema = models.ForeignKey(Tema, on_delete=models.CASCADE)


	def buscarMateria(self):
		materia=self.foraneaCurso.foraneaMateriaGrado
		return materia

	def __str__(self):
		return '{} {} {}'.format(self.idTarea,self.tituloTarea,self.fechaLimite)
	
	@property
	def filename(self):
		return self.rutaArchivo.name.rsplit('/', 1)[-1]
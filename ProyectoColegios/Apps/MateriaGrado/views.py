# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from Apps.MateriaGrado.models import MateriaGrado
from Apps.Curso.models import Curso
# Create your views here.


def cargarTemasTarea(idCurso):
	'''Este metodo retorna un conjunto con el idTema y el nombre del tema'''
	materiaGrado = buscarMateriaGrado(idCurso)
	temas = materiaGrado.tema_set.all()
	return temas

def buscarMateriaGrado(idCurso):
	materiaGrado = Curso.objects.get( idCurso = idCurso )
	return materiaGrado.foraneaMateriaGrado
	
